
#########################
# İş Problemi
#########################

# Türkiye’nin en büyük online hizmet platformu olan Armut, hizmet verenler ile hizmet almak isteyenleri buluşturmaktadır.
# Bilgisayarın veya akıllı telefonunun üzerinden birkaç dokunuşla temizlik, tadilat, nakliyat gibi hizmetlere kolayca
# ulaşılmasını sağlamaktadır.
# Hizmet alan kullanıcıları ve bu kullanıcıların almış oldukları servis ve kategorileri içeren veri setini kullanarak
# Association Rule Learning ile ürün tavsiye sistemi oluşturulmak istenmektedir.


#########################
# Veri Seti
#########################
# Veri seti müşterilerin aldıkları servislerden ve bu servislerin kategorilerinden oluşmaktadır.
# Alınan her hizmetin tarih ve saat bilgisini içermektedir.

# UserId: Müşteri numarası
# ServiceId: Her kategoriye ait anonimleştirilmiş servislerdir. (Örnek : Temizlik kategorisi altında koltuk yıkama servisi)
# Bir ServiceId farklı kategoriler altında bulanabilir ve farklı kategoriler altında farklı servisleri ifade eder.
# (Örnek: CategoryId’si 7 ServiceId’si 4 olan hizmet petek temizliği iken CategoryId’si 2 ServiceId’si 4 olan hizmet mobilya montaj)
# CategoryId: Anonimleştirilmiş kategorilerdir. (Örnek : Temizlik, nakliyat, tadilat kategorisi)
# CreateDate: Hizmetin satın alındığı tarih


import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 500)

#########################
# GÖREV 1: Veriyi Hazırlama
#########################
# Adım 1: armut_data.csv dosyasınız okutunuz.
# df = pd.read_csv("Recommendation_Systems/datasets/armut_data.csv")
df = pd.read_csv("C:/Users/BERNA/OneDrive/Masaüstü/Data_Scientist_and_AI/Recommendation_Systems/datasets/armut_data.csv")
def check_df(dataframe, head=5):
    print("############### Shape  ###############")
    print(dataframe.shape)
    print("############### Columns  ###############")
    print(dataframe.columns)
    print("############### Info  ###############")
    print(dataframe.info())
    print("############### Head  ###############")
    print(dataframe.head(head))
    print("############### NA  ###############")
    print(dataframe.isnull().sum())
    print("############### Quantiles  ###############")
    print(dataframe.describe([0, 0.85, 0.50, 0.95, 0.99, 1]).T)
check_df(df, 10)
# Adım 2: ServisID her bir CategoryID özelinde farklı bir hizmeti temsil etmektedir.
# ServiceID ve CategoryID'yi "_" ile birleştirerek hizmetleri temsil edecek yeni bir değişken oluşturunuz.
df["Hizmet"] = df["ServiceId"].astype(str) + "_" + df["CategoryId"].astype(str)

# II. YOL
df["Hizmet"] = df[["ServiceId", "CategoryId"]].apply(lambda x: str(x["ServiceId"]) + "_" + str(x["CategoryId"]), axis=1)

#  III. YOL
df["Hizmet"] = df[["ServiceId", "CategoryId"]].apply(lambda x:  f"{x.ServiceId}_{x.CategoryID}", axis=1)

# Adım 3: Veri seti hizmetlerin alındığı tarih ve saatten oluşmaktadır, herhangi bir sepet tanımı (fatura vb. ) bulunmamaktadır.
# Association Rule Learning uygulayabilmek için bir sepet (fatura vb.) tanımı oluşturulması gerekmektedir.
# Burada sepet tanımı her bir müşterinin aylık aldığı hizmetlerdir. Örneğin; 7256 id'li müşteri 2017'in 8.ayında aldığı 9_4, 46_4 hizmetleri bir sepeti;
# 2017’in 10.ayında aldığı  9_4, 38_4  hizmetleri başka bir sepeti ifade etmektedir. Sepetleri unique bir ID ile tanımlanması gerekmektedir.

# CreateDate sütununu datetime formatına dönüştürelim
df["CreateDate"] = pd.to_datetime(df["CreateDate"])
df.info()
# Bunun için öncelikle sadece yıl ve ay içeren yeni bir date değişkeni oluşturunuz.
df['New_Date'] = df['CreateDate'].dt.strftime('%Y-%m')
# UserID ve yeni oluşturduğunuz date değişkenini "_" ile birleştirirek SepetID adında yeni bir değişkene atayınız.
df["SepetID"] = df["UserId"].astype(str) + "_" + df["New_Date"]

# veri setini UserId', 'New_Date göre gruplayıp Hizmet verilerini getirelim istenilenleri bir sağlamasını yapalım :)
gruplanmis_sepetler = df.groupby(['UserId', 'New_Date'])['Hizmet'].apply(list).reset_index()
# 7256 numaralı kullanıcının verilerini filtreleyip istenilen değerlerle yorumlayalım.
kullanici_7256 = gruplanmis_sepetler[gruplanmis_sepetler['UserId'] == 7256]

#########################
# GÖREV 2: Birliktelik Kuralları Üretiniz
#########################

# Adım 1: Aşağıdaki gibi sepet hizmet pivot table’i oluşturunuz.

# Hizmet         0_8  10_9  11_11  12_7  13_11  14_7  15_1  16_8  17_5  18_4..
# SepetID
# 0_2017-08        0     0      0     0      0     0     0     0     0     0..
# 0_2017-09        0     0      0     0      0     0     0     0     0     0..
# 0_2018-01        0     0      0     0      0     0     0     0     0     0..
# 0_2018-04        0     0      0     0      0     1     0     0     0     0..
# 10000_2017-08    0     0      0     0      0     0     0     0     0     0..

# df = df[["Hizmet", "CategoryId", "ServiceId", "SepetID"]]
sepet_hizmet_piv_tab = df.pivot_table(columns="Hizmet", values=["ServiceId", "CategoryId"], index="SepetID",  aggfunc='count', fill_value=0)

# df.groupby(['SepetID', 'Hizmet'])['Hizmet'].count().unstack().fillna(0).applymap(lambda x: 1 if x > 0 else 0)
sepet_hizmet_piv_tab.columns
# CategoryId ve ServiceId sütunlarını kaldırma - seviye düşürme
sepet_hizmet_piv_tab.columns = sepet_hizmet_piv_tab.columns.droplevel()
# Pivot tablodaki benzersiz değerleri kontrol edin 0-1 den başka değerler var mı? bir bakalım :)
unique_values = sepet_hizmet_piv_tab.apply(pd.Series.unique)
# Pivot tablonuzu binary formata dönüştürün
pivot_binary = sepet_hizmet_piv_tab.apply(lambda x: x.map(lambda y: 1 if y > 0 else 0))

# Adım 2: Birliktelik kurallarını oluşturunuz.
pivot_binary = pivot_binary.astype(bool)  # veri setimiz apriori de daha iyi performans göstermesi iiçn bool tipine çevirdik.
# Her bir hizmet ve hizmetler için olasılıkları hesaplayalım.
frequent_itemsets = apriori(pivot_binary,
                            min_support=0.01,
                            use_colnames=True)

frequent_itemsets.sort_values("support", ascending=False)

rules = association_rules(frequent_itemsets,
                          metric="support",
                          min_threshold=0.01)

#  Kuralları lift değerine göre sıralıyoruz
sorted_rules = rules.sort_values("lift", ascending=False)
# Adım 3: arl_recommender fonksiyonunu kullanarak en son 2_0 hizmetini alan bir kullanıcıya hizmet önerisinde bulununuz.

def arl_recommender(rules_df, hizmet_id, rec_count=1, sort_value="lift"):
    sorted_rules = rules_df.sort_values(sort_value, ascending=False)
    recommendation_list = [list(rule.consequents)[0]
                            for rule in sorted_rules.itertuples()
                            if hizmet_id in rule.antecedents]

    return recommendation_list[0:rec_count]

arl_recommender(rules, '2_0', 2,"lift")
arl_recommender(rules, '2_0', 2,"confidence")

# II. YOL
def arl_recommender1(rules_df, product_id, sort_value="lift", rec_count=1):
    sorted_rules = rules_df.sort_values(sort_value, ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])
    return recommendation_list[0 : rec_count]

arl_recommender1(rules, '2_0',"confidence", 2)