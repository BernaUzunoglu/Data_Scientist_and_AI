############################################
# User-Based Collaborative Filtering
#############################################

# Adım 1: Veri Setinin Hazırlanması
# Adım 2: Öneri Yapılacak Kullanıcının İzlediği Filmlerin Belirlenmesi
# Adım 3: Aynı Filmleri İzleyen Diğer Kullanıcıların Verisine ve Id'lerine Erişmek
# Adım 4: Öneri Yapılacak Kullanıcı ile En Benzer Davranışlı Kullanıcıların Belirlenmesi
# Adım 5: Weighted Average Recommendation Score'un Hesaplanması
# Adım 6: Çalışmanın Fonksiyonlaştırılması

#############################################
# Adım 1: Veri Setinin Hazırlanması
#############################################
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)


def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv', nrows=50000)
    rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts()).reset_index()
    rare_movies = comment_counts[comment_counts["count"] <= 10000]["title"]
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df


user_movie_df = create_user_movie_df()

user_movie_df.head()
# bir tane kullanıcı seçelim
random_user = int(pd.Series(user_movie_df.index).sample(1, random_state=45).values)

#############################################
# Adım 2: Öneri Yapılacak Kullanıcının İzlediği Filmlerin Belirlenmesi
#############################################
random_user
user_movie_df.shape

random_user_df = user_movie_df[user_movie_df.index == random_user]
#  userin izlediği filmleri seçelim - sütunlarda NaN olmayanları getir.
movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()
# Gelen verilerden birisini kontrol edelim kullanıcının izleyip izlemediğini
user_movie_df.loc[user_movie_df.index == random_user,
                  user_movie_df.columns == "Fifth Element, The (1997)"]

# Kullanıcı kaç adet film izlemiş
len(movies_watched)

#############################################
# Adım 3: Aynı Filmleri İzleyen Diğer Kullanıcıların Verisine ve Id'lerine Erişmek
#############################################
# user_movie_df den izlenen filmleri bulup veri setini indirgeyelim.
movies_watched_df = user_movie_df[movies_watched]
user_movie_df.shape  # 462 tane film var
movies_watched_df.shape  # 191 tane filme indirgedik

# movies_watched_df Traspozunu alıp kullanıcıların kaç tane film izlemiş olduklarını bulalım.
user_movie_count = movies_watched_df.T.notnull().sum()

user_movie_count = user_movie_count.reset_index()

user_movie_count.columns = ["userId", "movie_count"]
user_movie_count.mean()
# seçilen user ile en az 20 filmi izleyen kullanıcılar
user_movie_count[user_movie_count["movie_count"] > 125].sort_values("movie_count", ascending=False)

user_movie_count[user_movie_count["movie_count"] == 150].count()

users_same_movies = user_movie_count[user_movie_count["movie_count"] > 125]["userId"]

# users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]
# perc = len(movies_watched) * 60 / 100

#############################################
# Adım 4: Öneri Yapılacak Kullanıcı ile En Benzer Davranışlı Kullanıcıların Belirlenmesi
#############################################

# Bunun için 3 adım gerçekleştireceğiz:
# 1. Sinan ve diğer kullanıcıların verilerini bir araya getireceğiz.
# 2. Korelasyon df'ini oluşturacağız.
# 3. En benzer kullanıcıları (Top Users) bulacağız

# isin ile movies_watched_df indexindeki değerlerin users_same_movies listesinde yer laıp almadığı kontrol edilir.
# final_df = pd.concat([movies_watched_df[movies_watched_df.index.isin(users_same_movies)], random_user_df[movies_watched]])

#  HATA : final_df hazırlanırken, concat kullanılarak zaten random user üzerinden hazırlanan movies_watched_df'ine ve user_same_movies serisine tekrar, random user tarafından izlenilen filmler eklenmekte. Bu da indislerde tekrara neden olduğu için unstack() methodunda sorun oluşturdu

final_df = movies_watched_df[movies_watched_df.index.isin(users_same_movies)]
final_df.head(1)
# Kullanıcıları sütunlara alalım.
corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()

corr_df = pd.DataFrame(corr_df, columns=["corr"])

corr_df.index.names = ['user_id_1', 'user_id_2']

corr_df = corr_df.reset_index()

top_users = corr_df[(corr_df["user_id_1"] == random_user) & (corr_df["corr"] >= 0.35)][
    ["user_id_2", "corr"]].reset_index(drop=True)

top_users = top_users.sort_values(by='corr', ascending=False)

top_users.rename(columns={"user_id_2": "userId"}, inplace=True)

#  Kullanıcılar filmlere ne kadar puan verdi
rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')

# Seçilen kullanıcıyı listeden çıkaralım
top_users_ratings = top_users_ratings[top_users_ratings["userId"] != random_user]

#############################################
# Adım 5: Weighted Average Recommendation Score'un Hesaplanması
#############################################
# Korelasyon ve rating değerlerinin ikisinide göz önünde bulunduralım.
top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']

top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})

recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})

recommendation_df = recommendation_df.reset_index()

recommendation_df[recommendation_df["weighted_rating"] > 1.9]

movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > 1.9].sort_values("weighted_rating",
                                                                                                   ascending=False)

movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv', nrows=50000)
# Sinanın beğenebileceği filmler ve isimlerini getirelim
movies_to_be_recommend.merge(movie[["movieId", "title"]])


#############################################
# Adım 6: Çalışmanın Fonksiyonlaştırılması
#############################################

def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv', nrows=50000)
    rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts()).reset_index()
    rare_movies = comment_counts[comment_counts["count"] <= 10000]["title"]
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df


user_movie_df = create_user_movie_df()


# perc = len(movies_watched) * 60 / 100
# users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]


def user_based_recommender(random_user, user_movie_df, ratio=60, cor_th=0.65, score=3.5):
    import pandas as pd
    random_user_df = user_movie_df[user_movie_df.index == random_user]
    movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()
    movies_watched_df = user_movie_df[movies_watched]
    user_movie_count = movies_watched_df.T.notnull().sum()
    user_movie_count = user_movie_count.reset_index()
    user_movie_count.columns = ["userId", "movie_count"]
    perc = len(movies_watched) * ratio / 100
    users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]

    final_df = movies_watched_df[movies_watched_df.index.isin(users_same_movies)]

    corr_df = final_df.T.corr().unstack().sort_values().drop_duplicates()
    corr_df = pd.DataFrame(corr_df, columns=["corr"])
    corr_df.index.names = ['user_id_1', 'user_id_2']
    corr_df = corr_df.reset_index()

    top_users = corr_df[(corr_df["user_id_1"] == random_user) & (corr_df["corr"] >= cor_th)][
        ["user_id_2", "corr"]].reset_index(drop=True)

    top_users = top_users.sort_values(by='corr', ascending=False)
    top_users.rename(columns={"user_id_2": "userId"}, inplace=True)
    rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')

    top_users_ratings = top_users.merge(rating[["userId", "movieId", "rating"]], how='inner')
    top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']

    recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})
    recommendation_df = recommendation_df.reset_index()

    movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > score].sort_values(
        "weighted_rating", ascending=False)
    movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv', nrows=50000)
    return movies_to_be_recommend.merge(movie[["movieId", "title"]])


random_user = int(pd.Series(user_movie_df.index).sample(1).values)
user_based_recommender(random_user, user_movie_df, cor_th=0.50, score=4)
