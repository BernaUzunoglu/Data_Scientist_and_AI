
#############################################
# PROJE: Hybrid Recommender System
#############################################

# ID'si verilen kullanıcı için item-based ve user-based recomennder yöntemlerini kullanarak tahmin yapınız.
# 5 öneri user-based modelden 5 öneri de item-based modelden ele alınız ve nihai olarak 10 öneriyi 2 modelden yapınız.

import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
#############################################
# Görev 1: Verinin Hazırlanması
#############################################
# Adım 1: Movie ve Rating veri setlerini okutunuz.
# movieId, film adı ve filmin tür bilgilerini içeren veri seti
movie_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv')
# UserID, film adı, filme verilen oy ve zaman bilgisini içeren veri seti
rating_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
rating_df.head()

# Adım 2: Rating veri setine filmlerin isimlerini ve türünü movie film setini kullanrak ekleyiniz.
# Ratingdeki kullanıcıların oy kullandıkları filmlerin sadece id'si var.
# Idlere ait film isimlerini ve türünü movie veri setinden ekliyoruz.

# Veri setlerini movieID kolonuna göre birleştirme
rating_movie_df = pd.merge(rating_df, movie_df, on='movieId', how='left')
rating_movie_df.head()
rating_movie_df.shape
# Adım 3: Herbir film için toplam kaç kişinin oy kullandığını hesaplayınız.Toplam oy kullanılma sayısı 1000'un altında olan filmleri veri setinden çıkarınız.
# Herbir film için toplam kaç kişinin oy kullanıldığını hesaplıyoruz.
movie_counts = pd.DataFrame(rating_movie_df["title"].value_counts()).reset_index()

# Toplam oy kullanılma sayısı 1000'in altında olan filmlerin isimlerini rare_movies de tutuyoruz.
rare_movies = movie_counts[movie_counts["count"] <= 1000]["title"]

# Ve veri setinden çıkartıyoruz
common_movies = rating_movie_df[~rating_movie_df["title"].isin(rare_movies)]
common_movies.shape
rating_movie_df["title"].nunique()
common_movies["title"].nunique()

# Yalnızca gerekli sütunları seçelim
# common_movies = common_movies[['userId', 'title', 'rating']]

# Adım 4: # index'te userID'lerin sutunlarda film isimlerinin ve değer olarakta ratinglerin bulunduğu
# dataframe için pivot table oluşturunuz.
user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

# Adım 5: Yukarıda yapılan tüm işlemleri fonksiyonlaştıralım
def create_user_movie_df():
    movie_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv')
    rating_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')
    rating_movie_df = pd.merge(rating_df, movie_df, on='movieId', how='left')
    movie_counts = pd.DataFrame(rating_movie_df["title"].value_counts()).reset_index()
    rare_movies = movie_counts[movie_counts["count"] <= 10000]["title"]
    common_movies = rating_movie_df[~rating_movie_df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df

user_movie_df = create_user_movie_df()
user_movie_df.head()
user_movie_df.shape
#############################################
# Görev 2: Öneri Yapılacak Kullanıcının İzlediği Filmlerin Belirlenmesi
#############################################
# Adım 1: Rastgele bir kullanıcı id'si seçiniz.
random_user = int(pd.Series(user_movie_df.index).sample(1, random_state=45).values)

# Adım 2: Seçilen kullanıcıya ait gözlem birimlerinden oluşan random_user_df adında yeni bir dataframe oluşturunuz.
random_user_df = user_movie_df[user_movie_df.index == random_user]

# Adım 3: Seçilen kullanıcının oy kullandığı filmleri movies_watched adında bir listeye atayınız. Yani NaN olmayan değerleri getirelim.
movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()
len(movies_watched)
#############################################
# Görev 3: Aynı Filmleri İzleyen Diğer Kullanıcıların Verisine ve Id'lerine Erişmek
#############################################
# Adım 1: Seçilen kullanıcının izlediği fimlere ait sutunları user_movie_df'ten seçiniz ve movies_watched_df adında yeni bir dataframe oluşturuyoruz.
movies_watched_df = user_movie_df[movies_watched]
movies_watched_df.shape
# Adım 2: Herbir kullancının seçili user'in izlediği filmlerin kaçını izlediği bilgisini taşıyan user_movie_count adında yeni bir dataframe oluşturunuz.
# Ve yeni bir df oluşturuyoruz.
user_movie_count = movies_watched_df.T.notnull().sum()
user_movie_count = user_movie_count.reset_index()
# Sütun isimlerini düzeltelim
user_movie_count.columns = ["userId", "movie_count"]

# Adım 3: Seçilen kullanıcının oy verdiği filmlerin yüzde 60 ve üstünü izleyenleri benzer kullanıcılar olarak görüyoruz.
# Bu kullanıcıların id’lerinden users_same_movies adında bir liste oluşturunuz.
perc = len(movies_watched) * 60 / 100
users_same_movies = user_movie_count[user_movie_count["movie_count"] > perc]["userId"]

#############################################
# Görev 4: Öneri Yapılacak Kullanıcı ile En Benzer Kullanıcıların Belirlenmesi
#############################################
# Adım 1: user_same_movies listesi içerisindeki seçili user ile benzerlik gösteren kullanıcıların id’lerinin bulunacağı şekilde movies_watched_df dataframe’ini filtreleyiniz.
movies_watched_df = movies_watched_df[movies_watched_df.index.isin(users_same_movies)]

# Adım 2: Kullanıcıların birbirleri ile olan korelasyonlarının bulunacağı yeni bir corr_df dataframe’i oluşturunuz.
# Kullanıcıları sütunlara alalım.
corr_df = movies_watched_df.T.corr().unstack().sort_values().drop_duplicates()

corr_df = pd.DataFrame(corr_df, columns=["corr"])

corr_df.index.names = ['user_id_1', 'user_id_2']

corr_df = corr_df.reset_index()
# random user diğer user ile korelasyonuna bakalım
corr_df[corr_df["user_id_1"] == random_user]

# Adım 3: Seçili kullanıcı ile yüksek korelasyona sahip (0.65’in üzerinde olan) kullanıcıları filtreleyerek top_users adında yeni bir dataframe oluşturunuz.
top_users = corr_df[(corr_df["user_id_1"] == random_user) & (corr_df["corr"] >= 0.60)][
    ["user_id_2", "corr"]].reset_index(drop=True)

top_users = top_users.sort_values(by='corr', ascending=False)

top_users.rename(columns={"user_id_2": "userId"}, inplace=True)

# Adım 4:  top_users dataframe’ine rating veri seti ile merge ediniz
top_users_ratings = top_users.merge(rating_df[["userId", "movieId", "rating"]], how='inner')

#############################################
# Görev 5: Weighted Average Recommendation Score'un Hesaplanması ve İlk 5 Filmin Tutulması
#############################################
# Adım 1: Her bir kullanıcının corr ve rating değerlerinin çarpımından oluşan weighted_rating adında yeni bir değişken oluşturunuz.
top_users_ratings['weighted_rating'] = top_users_ratings['corr'] * top_users_ratings['rating']

# Adım 2: Film id’sive her bir filme ait tüm kullanıcıların weighted rating’lerinin ortalama değerini içeren recommendation_df adında yeni bir
# dataframe oluşturunuz.
recommendation_df = top_users_ratings.groupby('movieId').agg({"weighted_rating": "mean"})
recommendation_df = recommendation_df.reset_index()
# Adım 3: Adım3: recommendation_df içerisinde weighted rating'i 3.5'ten büyük olan filmleri seçiniz ve weighted rating’e göre sıralayınız.
# İlk 5 gözlemi movies_to_be_recommend olarak kaydediniz.
movies_to_be_recommend = recommendation_df[recommendation_df["weighted_rating"] > 3.5].sort_values("weighted_rating", ascending=False).head(5)

# Adım 4:  Tavsiye edilen 5 filmin isimlerini getiriniz.
movies_to_be_recommend.merge(movie_df[["movieId", "title"]])


#############################################
# Adım 6: Item-Based Recommendation
#############################################

# Kullanıcının en son izlediği ve en yüksek puan verdiği filmin adına göre item-based öneri yapınız.
# user = 108170
user = random_user
# Adım 1: movie,rating veri setlerini okutunuz.
movie_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/movie.csv')
rating_df = pd.read_csv('Recommendation_Systems/datasets/movie_lens_dataset/rating.csv')

# Adım 2: Öneri yapılacak kullanıcının 5 puan verdiği filmlerden puanı en güncel olan filmin id'sinin alınız.
movie_id = rating_df[(rating_df["userId"] == user) & (rating_df["rating"] == 5.0)].sort_values("timestamp", ascending=False).head(1)["movieId"]
# loc ile seçme
movie_id = rating_df.loc[(rating_df["userId"] == user) & (rating_df["rating"] == 5.0)].sort_values("timestamp", ascending=False).head(1)["movieId"]
rating_df.info()
type(movie_id)  # pandas.core.series.Series dönüyor idye iloc ile ulaşmak gerek
movie_id.iloc[0]

# Adım 3 :User based recommendation bölümünde oluşturulan user_movie_df dataframe’ini seçilen film id’sine göre filtreleyiniz.
user_movie_df
# user_movie_df de movie_Id si olmadığı için filtreleme yapabilmek için movieId sine göre filmin adını bulmak gerek.
movie_name = movie_df.loc[movie_df["movieId"] == movie_id.iloc[0]]["title"]
movie_df.info()
# filtreleme yapalım
movie_name_df = user_movie_df[movie_name]
# Adım 4: Filtrelenen dataframe’i kullanarak seçili filmle diğer filmlerin korelasyonunu bulunuz ve sıralayınız.
type(movie_name_df)
corr_movies = user_movie_df.corrwith(movie_name_df).sort_values(ascending=False)

# Adım 5: Seçili film’in kendisi haricinde ilk 5 film’I öneri olarak veriniz.

corr_movies[1:6]