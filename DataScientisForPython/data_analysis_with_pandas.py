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

df = pd.read_csv("DataScientisForPython/datasets/nba.csv")
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
df["Position"].head()
df["Position"].value_counts()  # Kategorik verilerden kaç adet var?

#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)

df.head()
df.index
df[0:13]
df.drop(0, axis=0).head()  #axis satır demek
delete_index = [1, 3, 5, 7]
df.drop(delete_index, axis=0).head(10) # bu silme işlemi kalıcı değildir

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
df["age2"] = df["age"]**2
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

