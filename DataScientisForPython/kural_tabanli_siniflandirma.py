import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("Display.float_format", lambda x: "%.2f" % x)

#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

# ################ Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

# ################ Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_csv("DataScientisForPython/datasets/persona.csv")
df.head()
df.info()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df['SOURCE'].unique()
df[['SOURCE']].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?
df['PRICE'].unique()
df[['PRICE']].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df['PRICE'].value_counts()
df.groupby("PRICE").size()
df.groupby("PRICE").count()
# pivot_table kullanarak her bir 'PRICE' değerinden kaç tane olduğunu saymak
price_counts = df.pivot_table(index='PRICE', aggfunc='size')
df.groupby("PRICE").agg("count")

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df.groupby("COUNTRY").aggregate("count")


def check_groupby(dataframe, groupby_column, agg_dict, sort_by=None, ascending=True, show_top_n=None):
    """
    DataFrame'de grup bazında toplu istatistikler hesaplar ve sonucu yazdırır.

    Args:
    dataframe (pd.DataFrame): İşlem yapılacak DataFrame.
    groupby_column (str): Gruplama işlemi yapılacak sütunun adı.
    agg_dict (dict): İstatistiksel işlemler sözlüğü (örneğin {'column1': 'sum', 'column2': 'mean'}).
    sort_by (str, optional): Sonucu sıralamak için kullanılacak sütun adı. Varsayılan None.
    ascending (bool, optional): Sıralamanın artan (True) veya azalan (False) şekilde olması. Varsayılan True.
    show_top_n (int, optional): Gösterilecek en üst N satır sayısı. Varsayılan None.

    Returns:
    pd.DataFrame: Gruplama ve istatistiksel işlemler sonrası DataFrame.
    """
    try:
        result = dataframe.groupby(groupby_column, observed=True).agg(agg_dict)

        if sort_by:
            result = result.sort_values(by=sort_by, ascending=ascending)

        if show_top_n:
            result = result.head(show_top_n)

        # print(result)
        return result

    except Exception as e:
        print(f"Bir hata oluştu: {e}")


check_groupby(df, 'COUNTRY', 'count')
# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").aggregate("sum")
check_groupby(df, 'COUNTRY', {"PRICE": "count"})

# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
df.head()
check_groupby(df, 'SOURCE', 'count')

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
check_groupby(df, 'COUNTRY', {'PRICE': 'mean'})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
check_groupby(df, 'SOURCE', {'PRICE': 'mean'})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
check_groupby(df, ['COUNTRY', 'SOURCE'], {'PRICE': 'mean'})

#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################
df.head()
check_groupby(df, ['COUNTRY', 'SOURCE', 'SEX', 'AGE'], {'PRICE': 'mean'}).head(30)
result1 = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean().reset_index()
result1.head(30)
#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
agg_df = check_groupby(df, ['COUNTRY', 'SOURCE', 'SEX', 'AGE'], {'PRICE': 'mean'}, 'PRICE', False)
agg_df.head(25)

#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)
agg_df.reset_index(inplace=True)
agg_df.head(15)

#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

# Panda'nın Cut() fonksiyonu dizi elemanlarını farklı kutulara ayırmak için kullanılır. Kesme işlevi esas olarak skaler veriler üzerinde istatistiksel analiz gerçekleştirmek için kullanılır.

# agg_df['AGE'] = agg_df['AGE'].astype('category')
# right=False parametresi, aralıkların sağ sınırının dahil edilmemesini sağlar (örneğin, 30 yaşı '19-30' aralığında değil, '31-45' aralığında yer alır)
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 30, 45, agg_df["AGE"].max()], labels=['0_18', '19_30', '31_45', '46_' + str(agg_df["AGE"].max())], right=False)

#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.
print(f"COUNTRY length: {len(df['COUNTRY'])}")
print(f"SOURCE length: {len(df['SOURCE'])}")
print(f"SEX length: {len(df['SEX'])}")
print(f"SEX length: {len(agg_df['SEX'])}")
print(f"AGE_CAT length: {len(agg_df['AGE_CAT'])}")

agg_df.info()
# ZIP ile yapımı NOT : Zip yapıla bilmesi için uzunluklar aynı olmalı
agg_df['CUSTOMERS_LEVEL_BASED'] = [f"{country}_{source}_{sex}_{age_cat}".upper() for country, source, sex, age_cat in zip(agg_df['COUNTRY'], agg_df['SOURCE'], agg_df['SEX'], agg_df['AGE_CAT'])]

# apply - lambda ile yapımı
agg_df.drop('CUSTOMERS_LEVEL_BASED', axis=1, inplace=True)
agg_df['CUSTOMERS_LEVEL_BASED'] = agg_df.apply(lambda row: f"{row['COUNTRY']}_{row['SOURCE']}_{row['SEX']}_{row['AGE_CAT']}".upper(), axis=1)

# join ve lambda ile yapımı
agg_df["CUSTOMER_LEVEL_BASED"] = agg_df[["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].agg(lambda x: "_".join(x).upper(), axis=1)

check_groupby(agg_df, 'CUSTOMERS_LEVEL_BASED', {'PRICE': ['mean', 'count']})

#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500)

# agg_df['PRICE'] bölümlere ayrılacak sütun
# q:4 istediğimiz çeyreklik sayısını ifade ediyor
# labels : bölğnen gruplar için etiket oluşturuyor.
agg_df["SEGMENT"] = pd.qcut(agg_df['PRICE'], 4, labels=['D', 'C', 'B', 'A'])
agg_df['PRICE'].max()
agg_df['PRICE'].min()
check_groupby(agg_df, 'SEGMENT', {'PRICE': ['max', 'min']})
check_groupby(agg_df, 'SEGMENT', {'PRICE': ['mean', 'max', 'sum']})
check_groupby(agg_df, 'SEGMENT', 'count')


#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
agg_df.head(30)
#  Alternatif örnek 33 yaşında ANDROID kullanan bir Türk kadınlar listesi
var = agg_df[(agg_df['SOURCE'] == 'android') & (agg_df['SEX'] == 'female') & (agg_df["AGE"] == 33)]

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_45"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user]["PRICE"].mean()
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user1 = "FRA_IOS_FEMALE_31_45"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user1]["PRICE"].mean()
