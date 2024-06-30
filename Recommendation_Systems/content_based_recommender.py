#############################
# Content Based Recommendation (İçerik Temelli Tavsiye)
#############################

#############################
# Film Overview'larına Göre Tavsiye Geliştirme
#############################

# 1. TF-IDF Matrisinin Oluşturulması
# 2. Cosine Similarity Matrisinin Oluşturulması
# 3. Benzerliklere Göre Önerilerin Yapılması
# 4. Çalışma Scriptinin Hazırlanması

#################################
# 1. TF-IDF Matrisinin Oluşturulması
#################################
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
# https://www.kaggle.com/rounakbanik/the-movies-dataset
df = pd.read_csv("Recommendation_Systems/datasets/the_movies_dataset/movies_metadata.csv", low_memory=False)  # Büyük bir veri seti olduğu için DtypeWarning kapamak icin
df.head()
df.shape

df["overview"].head()

tfidf = TfidfVectorizer(stop_words="english")  #stop_words ile dilde yaygınca kullanılan ve ölçüm değeri taşımayan verileri sil.

# df[df['overview'].isnull()]
df['overview'] = df['overview'].fillna('')  #boş overviewleri boşluk ile doldur.

# uygulanan değişiklliği dönüştürelim - ilk 10000 belgeyi kullanalım
tfidf_matrix = tfidf.fit_transform(df['overview'][:10000])

tfidf_matrix.shape  # (45466, 75827) (fimler-metinler-overview, benzersiz kelimeler)

df['title'].shape

# tfidf deki featureları(kolonları) getirelim
tfidf.get_feature_names_out()

tfidf_matrix.toarray()


#################################
# 2. Cosine Similarity Matrisinin Oluşturulması
#################################

cosine_sim = cosine_similarity(tfidf_matrix,
                               tfidf_matrix)

cosine_sim.shape
cosine_sim[1]


#################################
# 3. Benzerliklere Göre Önerilerin Yapılması
#################################
# Pandas serisis içerisine filmlerin isimlerini yerleştirelim.
df_subset = df.iloc[:10000]
indices = pd.Series(df_subset.index, index=df_subset['title'])

indices.index.value_counts()
# title larda çoklanmış değerlerden kurtulalım önceki filmleri çıkarıcaz
indices = indices[~indices.index.duplicated(keep='last')]

indices["Cinderella"]

indices["Sherlock Holmes"]

movie_index = indices["Cinderella"]

# Sherlock Holmes filmi ile diğer filmler arası benzerliğe erişelim.
cosine_sim[movie_index]
# daha okunabilir bir df oluşturalım.
similarity_scores = pd.DataFrame(cosine_sim[movie_index],
                                 columns=["score"])

movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index

# Cinderella izleyen kişiye önerilecek filmleri getir
df['title'].iloc[movie_indices]

#################################
# 4. Çalışma Scriptinin Hazırlanması
#################################

def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    movie_index = indices[title]
    # title'a gore benzerlik skorlarını hesapalama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])
    # kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return dataframe['title'].iloc[movie_indices]

content_based_recommender("Sherlock Holmes", cosine_sim, df)

content_based_recommender("The Matrix", cosine_sim, df)
# God Father ile önerilecek filmler
content_based_recommender("The Godfather", cosine_sim, df)

content_based_recommender('The Dark Knight Rises', cosine_sim, df)


def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['overview'] = dataframe['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['overview'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


cosine_sim = calculate_cosine_sim(df)
content_based_recommender('The Dark Knight Rises', cosine_sim, df)
# 1 [90, 12, 23, 45, 67]
# 2 [90, 12, 23, 45, 67]
# 3
