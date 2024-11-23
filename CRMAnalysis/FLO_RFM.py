###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# Alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################
import datetime as dt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################
# 1. flo_data_20K.csv verisini okuyunuz.
df_ = pd.read_csv("CRMAnalysis/datasets/flo_data_20k.csv")
df = df_.copy()

# 2. Veri setinde
# a. İlk 10 gözlem,
df.head(10)
# b. Değişken isimleri,
var = df.columns
# c. Boyut,
df.shape
# d. Betimsel istatistik,
df.describe().T
# e. Boş değer,
df.isnull().sum()
# f. Değişken tipleri, incelemesi yapınız.
df.info()

# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.
df['total_transaction_count'] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df['total_spend'] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
# last_order_date sütununu datetime tipine çevirme
# df['last_order_date'] = pd.to_datetime(df['last_order_date']) or # df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)
for column in df.columns:
    if 'date' in column:
        df[column] = pd.to_datetime(df[column])


# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız.
df.groupby("order_channel").agg({"master_id": "count",
                                 "total_transaction_count": "sum",
                                 "total_spend": "sum"})

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
df.sort_values(by="total_spend", ascending=False)[["master_id", "total_spend"]].head(10)

# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
df.sort_values(by="total_transaction_count", ascending=False)[["master_id", "total_transaction_count"]].head(10)


# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
df.isnull().sum()


def preprocess_data(dataframe, head):
    print("############### Shape  ###############")
    print(dataframe.shape)
    print("############### DF Info  ###############")
    print(dataframe.info())
    print("############### Describe  ###############")
    print(dataframe.describe().T)
    print("############### Types  ###############")
    print(dataframe.dtypes)
    print("############### Head  ###############")
    print(dataframe.head(head))
    print("############### Tail  ###############")
    print(dataframe.tail(head))
    print("############### NA  ###############")
    # Eksik değerli verileri silme işlemi.
    dataframe.dropna(inplace=True)
    print(dataframe.isnull().sum())
    print("############### Converting to Date  ###############")
    for column in dataframe.columns:
        if 'date' in column:
            dataframe[column] = pd.to_datetime(dataframe[column])
            print(f"Tarih formatına çevirilen değişken:  {column}")
    print("############### Quantiles  ###############")
    print(dataframe.describe([0, 0.85, 0.50, 0.95, 0.99, 1]).T)


preprocess_data(df, 10)

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################
# Recency => Analizin Yapıldığı Tarih - İlgili Müş. Son Sat. Tar.
# Frequency => Toplam satın alma
# Monetary => Müşterinin satın alma sonucunda bıraktığı toplam parasal değerdir.

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi
df.head()
today_date = df["last_order_date"].max() + dt.timedelta(days=2)  # Analiz tarihi
df.head()

# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe
# Eğer master id tekilleştirilmemiş olsaydı bu şekilde group by ile tekilleştirecektik.
# rfm = df.groupby('master_id').agg({'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
#                                    'total_transaction_count': lambda total_transaction_count: total_transaction_count.nunique(),
#                                    'total_spend': lambda total_spend: total_spend.sum()})
#

df['last_order_date'] = df['last_order_date'].apply(lambda x: (today_date - x).days)
# Adım 3: Hesapladığınız metrikleri rfm isimli bir değişkene atayınız
rfm = df.loc[:, ['master_id', 'last_order_date', 'total_transaction_count', 'total_spend']]
df.head()
rfm.head()

# Adım 4: Oluşturduğunuz metriklerin isimlerini recency, frequency ve monetary olarak değiştiriniz.
rfm = rfm.rename(columns={'last_order_date': 'recency', 'total_transaction_count': 'frequency', 'total_spend': 'monetary'})
rfm.describe().T

# Monotery değerinde 0 altında değer var mı kontrolü.
has_negative_values = (rfm['monetary'] < 0).any()
rfm.shape

###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi
# Recency değişkeni küçükten büyüğe sıralar.Çeyreklere böler.
rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
# 0-100, 0-20, 20-40, 40-60, 60-80, 80-100
# rank() fonksiyonu, pandas kütüphanesinde kullanılan bir yöntemdir ve DataFrame veya Series içindeki verilerin sıralamasını belirler. Bu fonksiyon, belirli bir eksene göre elemanların sıralamasını numaralandırır ve aynı değere sahip elemanlara aynı sıralama numarasını verir.
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi
rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

rfm.describe().T
# Şampiyon müşteriler
rfm[rfm["RF_SCORE"] == "55"]
# Göreceli olarak daha az önemli müşteriler
rfm[rfm["RF_SCORE"] == "11"]

###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)

###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık(champions, loyal_customers)  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.
df.head()
# "interested_in_categories_12" sütununda "KADIN" kelimesini içeren satırları getirme
filtered_woman_df = df[df['interested_in_categories_12'].str.contains('KADIN')]  # 7603 rows kayıt geldi

# İki DataFrame'i birleştirme
merged_df = pd.merge(rfm, filtered_woman_df, on='master_id', how='inner')
# champions ve loyal customer sayısını bulalım => 2497 tane kayıt var
segment_counts = merged_df['segment'].value_counts()

# "Segmentation" sütunu "champions" veya "loyal_customers" olan satırları filtreleme
# isin() fonksiyonu, bir pandas Serisi veya DataFrame'in belirli değerlere sahip satırlarını filtrelemek için kullanılır.
filtered_df = merged_df[merged_df['segment'].isin(['champions', 'loyal_customers'])]


# yeni_marka_hedef_musteri_id = pd.DataFrame()
yeni_marka_hedef_musteri_id = filtered_df["master_id"].reset_index(drop=True)

# csv olarak kaydetme
yeni_marka_hedef_musteri_id.to_csv("yeni_marka_hedef_musteri_id.csv")

# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.
df.head()
filtered_man_child_df = df[df['interested_in_categories_12'].str.contains('ERKEK|COCUK')]
# İki DataFrame'i birleştirme
merged_df = pd.merge(rfm, filtered_man_child_df, on='master_id', how='inner')
# champions ve loyal customer sayısını bulalım => Toplam 1759 tane kayıt var
segment_counts1 = merged_df['segment'].value_counts()

# "Segmentation" sütunu "cant_loose, 'cant_loose" veya "about_to_sleep"  olan satırları filtreleme
# isin() fonksiyonu, bir pandas Serisi veya DataFrame'in belirli değerlere sahip satırlarını filtrelemek için kullanılır.
filtered_df = merged_df[merged_df['segment'].isin(['cant_loose', 'about_to_sleep', 'new_customers'])]


# yeni_marka_hedef_musteri_id = pd.DataFrame()
indirim_hedef_musteri_id = filtered_df["master_id"].reset_index(drop=True)

# csv olarak kaydetme
indirim_hedef_musteri_id.to_csv("indirim_hedef_musteri_id.csv")

# GÖREV 6: Tüm süreci fonksiyonlaştırınız.
def create_rfm(dataframe):
    # Veriyi Hazırlma
    dataframe["order_num_total"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_online"]
    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)


    # RFM METRIKLERININ HESAPLANMASI
    dataframe["last_order_date"].max()  # 2021-05-30
    # analysis_date = dt.datetime(2021, 6, 1)
    analysis_date =  dataframe["last_order_date"].max() + dt.timedelta(days=2)
    rfm = pd.DataFrame()
    rfm["customer_id"] = dataframe["master_id"]
    rfm["recency"] = (analysis_date - dataframe["last_order_date"]).dt.days
    rfm["frequency"] = dataframe["order_num_total"]
    rfm["monetary"] = dataframe["customer_value_total"]

    # RF ve RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])
    rfm["RF_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str) + rfm['monetary_score'].astype(str))


    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_Risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }
    rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)

    return rfm[["customer_id", "recency","frequency","monetary","RF_SCORE","RFM_SCORE","segment"]]

rfm_df = create_rfm(df)
