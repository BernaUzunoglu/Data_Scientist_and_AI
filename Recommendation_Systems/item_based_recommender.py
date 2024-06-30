###########################################
# Item-Based Collaborative Filtering
###########################################

# Veri seti: https://grouplens.org/datasets/movielens/

# Adım 1: Veri Setinin Hazırlanması
# Adım 2: User Movie Df'inin Oluşturulması
# Adım 3: Item-Based Film Önerilerinin Yapılması
# Adım 4: Çalışma Scriptinin Hazırlanması

######################################
# Adım 1: Veri Setinin Hazırlanması
######################################
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
df = movie.merge(rating, how="left", on="movieId")  #movie sol  tarafta rating sağ tarafta
movie.head()
rating.head()
df.head()


######################################
# Adım 2: User Movie Df'inin Oluşturulması
######################################

df.head()
df.shape
# eşsiz film sayısı
df["title"].nunique()
# filmlerin aldığı rating sayısı
df["title"].value_counts().head()

comment_counts = pd.DataFrame(df["title"].value_counts()).reset_index()
# Az rate sahip filmleri bulalım.
rare_movies = comment_counts[comment_counts["count"] <= 1000]["title"]
# Az oy almış filmleri dataframeden çıkaralım.
common_movies = df[~df["title"].isin(rare_movies)]
common_movies.shape
df["title"].nunique()
common_movies["title"].nunique()

# satırlarda kullanıcı id'si sütunlarda filmlerin olduğu bir pivot table oluşturalım.
user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

user_movie_df.shape
user_movie_df.columns


######################################
# Adım 3: Item-Based Film Önerilerinin Yapılması
######################################

movie_name = "Matrix, The (1999)"
movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)

# rasgele film seçme ve film önerme
movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


# Girilen keyword arıyıp olan filmleri getiren fonksiyon.
def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]

check_film("Insomnia", user_movie_df)


######################################
# Adım 4: Çalışma Scriptinin Hazırlanması
######################################

def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv')
    rating = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["title"] <= 10000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df

user_movie_df = create_user_movie_df()


def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)

item_based_recommender("Matrix, The (1999)", user_movie_df)

movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]

item_based_recommender(movie_name, user_movie_df)





