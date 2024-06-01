
###################################################
# PROJE: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# İş Problemi
###################################################

# E-ticaretteki en önemli problemlerden bir tanesi ürünlere satış sonrası verilen puanların doğru şekilde hesaplanmasıdır.
# Bu problemin çözümü e-ticaret sitesi için daha fazla müşteri memnuniyeti sağlamak, satıcılar için ürünün öne çıkması ve satın
# alanlar için sorunsuz bir alışveriş deneyimi demektir. Bir diğer problem ise ürünlere verilen yorumların doğru bir şekilde sıralanması
# olarak karşımıza çıkmaktadır. Yanıltıcı yorumların öne çıkması ürünün satışını doğrudan etkileyeceğinden dolayı hem maddi kayıp
# hem de müşteri kaybına neden olacaktır. Bu 2 temel problemin çözümünde e-ticaret sitesi ve satıcılar satışlarını arttırırken müşteriler
# ise satın alma yolculuğunu sorunsuz olarak tamamlayacaktır.

###################################################
# Veri Seti Hikayesi
###################################################

# Amazon ürün verilerini içeren bu veri seti ürün kategorileri ile çeşitli metadataları içermektedir.
# Elektronik kategorisindeki en fazla yorum alan ürünün kullanıcı puanları ve yorumları vardır.

# Değişkenler:
# reviewerID: Kullanıcı ID’si
# asin: Ürün ID’si
# reviewerName: Kullanıcı Adı
# helpful: Faydalı değerlendirme derecesi
# reviewText: Değerlendirme
# overall: Ürün rating’i
# summary: Değerlendirme özeti
# unixReviewTime: Değerlendirme zamanı - Unix zaman damgası ,1 Ocak 1970'ten bu yana geçen saniye sayısını temsil eder.
# reviewTime: Değerlendirme zamanı Raw
# day_diff: Değerlendirmeden itibaren geçen gün sayısı
# helpful_yes: Değerlendirmenin faydalı bulunma sayısı
# total_vote: Değerlendirmeye verilen oy sayısı

###############################
# Import İşlemleri
###############################
import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

###################################################
# GÖREV 1: Average Rating'i Güncel Yorumlara Göre Hesaplayınız ve Var Olan Average Rating ile Kıyaslayınız.
###################################################

# Paylaşılan veri setinde kullanıcılar bir ürüne puanlar vermiş ve yorumlar yapmıştır.
# Bu görevde amacımız verilen puanları tarihe göre ağırlıklandırarak değerlendirmek.
# İlk ortalama puan ile elde edilecek tarihe göre ağırlıklı puanın karşılaştırılması gerekmektedir.


###################################################
# Adım 1: Veri Setini Okutunuz ve Ürünün Ortalama Puanını Hesaplayınız.
###################################################
df = pd.read_csv("Measurement_Problems/datasets/amazon_review.csv")
print(df.shape)
df.info()
df.value_counts("asin")
df.isnull().sum()
df.head(20)
# df.tail(20)
# df["helpful"]
# df[df["reviewerID"] == "A12B7ZMXFI6IXY"]
df.groupby("asin").agg({"overall": "mean"})
df["overall"].mean()
###################################################
# Adım 2: Tarihe Göre Ağırlıklı Puan Ortalamasını Hesaplayınız.
###################################################
# Time-Based Weighted Average
df.head()
def time_based_weighted_average(dataframe, info=False, w1=30, w2=26, w3=24, w4=20):
    overall_means = [
        dataframe.loc[dataframe["day_diff"] <= 30, "overall"].mean() * w1 / 100,
        dataframe.loc[(dataframe["day_diff"] > 30) & (dataframe["day_diff"] <= 90), "overall"].mean() * w2 / 100,
        dataframe.loc[(dataframe["day_diff"] > 90) & (dataframe["day_diff"] <= 180), "overall"].mean() * w3 / 100,
        dataframe.loc[(dataframe["day_diff"] > 180), "overall"].mean() * w4 / 100]

    if info:
        time_intervals = ["0-30 gün", "30-90 gün", "90-180 gün", "180+ gün"]
        for interval, mean in zip(time_intervals, overall_means):
            print(f"{interval}: {mean}")
    return sum(overall_means)

time_based_weighted_average(df)

###################################################
# Adım 3: Ağırlıklandırılmış puanlamada her bir zaman diliminin ortalamasını karşılaştırıp yorumlayınız
###################################################
time_based_weighted_average(df, True)
###################################################
# Görev 2: Ürün için Ürün Detay Sayfasında Görüntülenecek 20 Review'i Belirleyiniz.
###################################################
df.head(10)
###################################################
# Adım 1. helpful_no Değişkenini Üretiniz
###################################################
df.sort_values("total_vote", ascending=False).head(20)
df.sort_values("total_vote", ascending=False).tail(20)
# Not:
# total_vote bir yoruma verilen toplam up-down sayısıdır.
# up, helpful demektir.
# veri setinde helpful_no değişkeni yoktur, var olan değişkenler üzerinden üretilmesi gerekmektedir.
# Toplam oy sayısından (total_vote) yararlı oy sayısı (helpful_yes) çıkarılarak yararlı bulunmayan oy sayılarını (helpful_no) bulunuz
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]
df.sort_values("helpful_no", ascending=False).head(20)
###################################################
# Adım 2. score_pos_neg_diff, score_average_rating ve wilson_lower_bound Skorlarını Hesaplayıp Veriye Ekleyiniz
###################################################
# score_pos_neg_diff, score_average_rating ve wilson_lower_bound skorlarını hesaplayabilmek için score_pos_neg_diff, score_average_rating ve wilson_lower_bound fonksiyonlarını tanımlayınız.
def score_pos_neg_diff(positive, negative):
    return positive - negative

def score_average_rating(positive, negative):
    if positive + negative == 0:
        return 0
    return positive / (positive + negative)

def wilson_lower_bound(positive, negative, confidence=0.95):
    n = positive + negative
    if n == 0:
        return 0
    # z-değeri, belirli bir güven aralığı (confidence interval) için kritik değeri belirler.
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * positive / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)

# score_pos_neg_diff'a göre skorlar oluşturunuz. Ardından; df içerisinde score_pos_neg_diff ismiyle kaydediniz.
# apply kullanarak sonucu hesaplayalım ve yeni bir sütun ekleyelim
df['score_pos_neg_diff'] = df.apply(lambda row: score_pos_neg_diff(row['helpful_yes'], row['helpful_no']), axis=1)

# score_average_rating'a göre skorlar oluşturunuz. Ardından; df içerisinde score_average_rating ismiyle kaydediniz.
df['score_average_rating'] = df.apply(lambda row: score_average_rating(row['helpful_yes'], row['helpful_no']), axis=1)

# wilson_lower_bound'a göre skorlar oluşturunuz. Ardından; df içerisinde wilson_lower_bound ismiyle kaydediniz.
df['wilson_lower_bound'] = df.apply(lambda row: wilson_lower_bound(row['helpful_yes'], row['helpful_no']), axis=1)

df.sort_values("score_pos_neg_diff", ascending=False).head()
df.sort_values("score_pos_neg_diff", ascending=False).tail()
df.sort_values("score_average_rating", ascending=False).head()
##################################################
# Adım 3. 20 Yorumu Belirleyiniz ve Sonuçları Yorumlayınız.
###################################################
# wilson_lower_bound'a göre ilk 20 yorumu belirleyip sıralayanız.
# Sonuçları yorumlayınız.

df.sort_values("wilson_lower_bound", ascending=False).head(20)
