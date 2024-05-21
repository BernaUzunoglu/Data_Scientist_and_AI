##########################
# PANDAS

# Pandas Serileri
import pandas as pd
import seaborn as sns

s = pd.Series([10, 77, 12, 4, 5])  # index li bir şekilde çıktı verir.
type(s)  #pandas.core.series.Series
s.index
s.dtype
s.size
s.ndim  #Pandas serileri tek boyutludur.
s.values  # Bir pandas serisinin valuelerine erişmek istediğimiz zaman index bilgilerine ulaşmak istemediğimiz için bize nump.array döner.
type(s.values)
s.head()
s.head(3)
s.tail()
s.tail(3)

######################################
# VERİ OKUMA

# df = pd.read_csv("DataScientisForPython/datasets/nba.csv")
df = pd.read_csv("C:/Users/BERNA/OneDrive/Masaüstü/Data_Scientist_and_AI/DataScientisForPython/datasets/nba.csv")
df.head()
# pandas cheatsheet

##############################
# Veriye Hızlı Bakış (Quick Look at Data)

df = sns.load_dataset("titanic")
df.head()
df.tail()
var = df.shape
df.info()
var1 = df.columns
df.index
df.describe().T  #  DataFrame'in sayısal sütunlarına ilişkin istatistiksel bir özet sağlar
df.isnull().values.any()  # DF values herhangi birinde bir tane dahi olsun boş değer var mı?
df.isnull().sum()  # Değişkenlerin eksiklik verileri
df["sex"].head()
df["sex"].value_counts()  # Kategorik verilerden kaç adet var?

#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)

df.head()
df.index
df[0:13]
df.drop(0, axis=0).head()  #axis satır demek
delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head(10)  # bu silme işlemi kalıcı değildir

# Kalıcı Silme
# df = df.drop(delete_index, axis=0)
# df.drop(delete_index, axis=0,inplace=True)  # Değişiklik yapıldığında kalıcı olsun istiyorsak inplace kullanır.


# Değişkeni Indexe Çevirmek
df["age"].head()
df.Age.head()
df.index = df["age"]
df.drop("age", axis=1).head()
df.drop("age", axis=1, inplace=True)
df.head()

# Indexi Değişkene Çevirmek I.YOL
df.index
# Data Frame df["Age"] şeklinde seçince böyle bir değişken yoksa bu durumda yeni değişken eklendiği anlaşılır.
df["age"] = df.index
df.drop("age", axis=1, inplace=True)  # Age değişkenini sildik.

# II. YOL
df = df.reset_index().head()

# Değişkenler Üzerinde İşlemler
pd.set_option('display.max_columns', None)  #Bütün kolonları göster
df = sns.load_dataset("titanic")
df.head()

var_mi = "age" in df  # Bu değişken veri seti içerisinde var mı ?

df["age"].head()  # Bu şekilde seçim yaparsak pandas serisi tipi döner.
df.age.head()
type(df.age.head())  # Pandas serisi

# Data Frame dönsünn istiyorsak seçimi şu şekilde yapmamız gerekiyor?
df[["age"]].head()
type(df[["age"]].head())

# Bir Data Frame içerisinden bir çok değişken seçme
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

# Data Frame değişken ekleme
df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / df["age2"]

# Bir değişkeni silmek
df.drop("age3", axis=1).head()
df.drop(col_names, axis=1).head()

# Değişkenler içinde belirli bir ifadeyi silme
# label base seçim - ~(tilda) işareti değil demek
df.loc[:, ~df.columns.str.contains("age")].head()  #age ifadesi dışındakileri seç demek

#######################
# loc - iloc yapıları # Dataframelerde seçim işlemleri için kul. özel yapılardır.
# loc : indexlerdeki labellara göre seçmek
# iloc : index bilgisi vererek seçim yapma işlemi (integer based selection)
#######################

df.head()
# iloc : integer based selection
df.iloc[0:3]
df.iloc[0:0]

# loc : label based selection
df.loc[0:3]

# Satırlardad 0-3 kadar sütunlardanda bir değişken seçmek istiyorum.
df.loc[0:3]
df.iloc[0:3, 3]
df.loc[0:3, "age"]

df.loc[0:3, col_names]

###########################
# Data Frame Koşullu Seçim (Conditional Selection)
###########################
df = sns.load_dataset("titanic")
# Veri setinde yaşı 50 den büyük olanlar.

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

# Yaşı 50 den büyük olanların sınıf verilerini getir.
df.loc[df["age"] > 50, "class"].head()

# Yaşı 50 den büyük olanların sınıf ve yaş verilerini getir.
df.loc[df["age"] > 50, ["class", "age"]].head()

# Yaşı 50 den büyük olanların erkeklerin verilerini getir.
df.loc[(df["age"] > 50) & (df["sex"] == "male")].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["class", "age"]].head()

# Yaş 50 den büyük,cinsiyet erkek ve liman Cherbourg olanları
df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"), ["class", "age"]].head()

df["embark_town"].value_counts()
# Yaş 50 den büyük,cinsiyet erkek ve liman Cherbourg yada Southampton olanları
df_new = df.loc[(df["age"] > 50)
                & (df["sex"] == "male")
                & ((df["embark_town"] == "Cherbourg")
                   | (df["embark_town"] == "Southampton")), ["class", "age", "embark_town"]].head()

df_new["embark_town"].value_counts()

####################################
#  Toplulaştırma ve Gruplama (Aggregation & Grouping)
###################################
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

df = sns.load_dataset("titanic")
df.head()

# Kadınların ve erkeklerin yaş ortalaması
df["age"].mean()  # yaş ortalaması

# Gruplamak istediğimiz değişkeni yazıp. Ortalama metonunun uygulanacağı değişkene uygula
df.groupby("sex")["age"].mean()

# Cinsiyete göre grupla , ortalam ve toplam bul
df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})
df.groupby("sex").agg({"age": ["mean", "sum"], "fare": "mean"})

df.groupby("sex").agg({"age": ["mean", "sum"], "embark_town": "count"})
df.groupby("sex").agg({"age": ["mean", "sum"], "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean", "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": "mean",
    "survived": "mean",
    "sex": "count"})

###########################
# Pivot Table
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex","embarked")  # Pivot table ön tanımlı fonk. mean dir.

# ÇIKTI
# embarked         C         Q         S
# sex
# female    0.876712  0.750000  0.689655
# male      0.305263  0.073171  0.174603

df.pivot_table("survived", "sex", "embarked", aggfunc="std")
df.pivot_table("survived", "sex", ["embarked", "class"])

# hem cinsiyet kırılım hem gemiiye binme hem yaş kırılımmı olsun. Fakat yaş kategorik bir değişken değil
# Yaş değişkenini kategorik değişkene çevir. cut ve qcut fonk. ile
# eğer değişkenleri tanıyorum kategoriliye biliyorsam cut , bilemiyorsam çeyreklere göre qcut kullanılır.
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.pivot_table("survived","sex","new_age")
df.pivot_table("survived","sex",["new_age", "class"])

pd.set_option("display.width", 500)

#######################
# Apply ve Lambda
# Apply : Satır yada sutunlarda otomatik olarak fonk. çalıştırma imkanı sağlar.
# Lambda : Fonk tanımlama şekli kullan at fonk kullanma imkanı sağlar.
######################


df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# Yukardaki işlemleri apply ve lambda ile yapalım.
df[["age", "age2", "age3"]].apply(lambda x: x/2).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/2).head()

# Sütunlarda age olanları bul age std hesapla
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Yapılan işlemleri yansıtmak
df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# Otomatik seçim örnek
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df.head()

########################
# Birleştirme(Join) İşlemleri

import numpy as np
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# Concat fonk. axis=0 tanımlı olduğu için DF'leri alt alta birleştirme yapar
pd.concat([df1, df2])  # Bu şekilde birleştirme işlemi yapıca index bilgilerini tutuyor. indexlerler beraber alt alta olduğu gibi birleştirme işlemi yapıyor.
pd.concat([df1, df2],ignore_index=True)  #Bu şekilde index bilgisini sıralı ilerlettik.

######################
# Merge ile Birleştirme İşlemleri

df3 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'groups': ['accounting', 'engineering', 'engineering', 'hr']})

df4 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df3, df4)
pd.merge(df3, df4, on="employees")

# Amaç : Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df5 = pd.merge(df3, df4)

df6 = pd.DataFrame({'groups': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
pd.merge(df5, df6)


data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
subset = df.loc[0:1, ['A', 'B']]
subset3 = df.loc[:, ['A', 'B']]

subset1 = df.iloc[0:2, [0, 1]]
subset2 = df.iloc[:, [0, 1]]