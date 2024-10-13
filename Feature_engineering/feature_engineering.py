#############################################
# FEATURE ENGINEERING & DATA PRE-PROCESSING
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)


def load_application_train():
    data = pd.read_csv("Feature_Engineering/datasets/application_train.csv")
    return data


dff = load_application_train()
dff.head()
dff.shape


def load():
    data = pd.read_csv("Feature_Engineering/datasets/titanic.csv")
    return data


df = load()
df.head()

#############################################
# 1. Outliers (Aykırı Değerler)
#############################################

#############################################
# Aykırı Değerleri Yakalama
#############################################

###################
# Grafik Teknikle Aykırı Değerler
###################

sns.boxplot(x=df["Age"])
plt.show()

###################
# Aykırı Değerler Nasıl Yakalanır?
###################

q1 = df["Age"].quantile(0.25)
q3 = df["Age"].quantile(0.75)  # 3 .çeyrek değer
iqr = q3 - q1
up = q3 + 1.5 * iqr
low = q1 - 1.5 * iqr

# Belirlediğimiz sınırların dışarısında kalan aykırı değerleri getirelim.
df[(df["Age"] < low) | (df["Age"] > up)]

# aykırı eğerlerin index değerlerine ulaşalım.
df[(df["Age"] < low) | (df["Age"] > up)].index

###################
# Aykırı Değer Var mı Yok mu?
###################

df[(df["Age"] < low) | (df["Age"] > up)].any(axis=None)
df[(df["Age"] < low)].any(axis=None)


# 1. Eşik değer belirledik.
# 2. Aykırılara eriştik.
# 3. Hızlıca aykırı değer var mı yok diye sorduk.

###################
# İşlemleri Fonksiyonlaştırmak
###################
# 05 - 95 ayarlamak veri setimizdeki ekstra ekstra aykırılarda işlem yapmak için iyi bir oran
def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


outlier_thresholds(df, "Age")
outlier_thresholds(df, "Fare")

low, up = outlier_thresholds(df, "Fare")

df[(df["Fare"] < low) | (df["Fare"] > up)].head()

df[(df["Fare"] < low) | (df["Fare"] > up)].index


# Aykırı değer var mı yok mu kontrol fonks.
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False


check_outlier(df, "Age")
check_outlier(df, "Fare")

###################
# grab_col_names
###################

dff = load_application_train()
dff.head()


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)

# PassengerId gibi pk olabilecek değişkenler nümerik değerlendirilemeyeceği için num_cols dan çıkartalım.
num_cols = [col for col in num_cols if col not in "PassengerId"]

for col in num_cols:
    print(col, check_outlier(df, col))

cat_cols, num_cols, cat_but_car = grab_col_names(dff)

num_cols = [col for col in num_cols if col not in "SK_ID_CURR"]

for col in num_cols:
    print(col, check_outlier(dff, col))


###################
# Aykırı Değerlerin Kendilerine Erişmek
###################

def grab_outliers(dataframe, col_name, index=False):
    low, up = outlier_thresholds(dataframe, col_name)

    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head())
    else:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))])

    if index:
        outlier_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return outlier_index


grab_outliers(df, "Age")

grab_outliers(df, "Age", True)

age_index = grab_outliers(df, "Age", True)

outlier_thresholds(df, "Age")
check_outlier(df, "Age")
grab_outliers(df, "Age", True)

#############################################
# Aykırı Değer Problemini Çözme
#############################################

###################
# Silme
###################

low, up = outlier_thresholds(df, "Fare")
df.shape

# Aykırı olmayan değerleri getirelim
df[~((df["Fare"] < low) | (df["Fare"] > up))].shape  # 775 tane aykırı olmayan gözlem değeri var.


def remove_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    df_without_outliers = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]
    return df_without_outliers


cat_cols, num_cols, cat_but_car = grab_col_names(df)

num_cols = [col for col in num_cols if col not in "PassengerId"]

df.shape

for col in num_cols:
    new_df = remove_outlier(df, col)

# 116 tane aykırı gözlem değeri varmış
df.shape[0] - new_df.shape[0]

###################
# Baskılama Yöntemi (re-assignment with thresholds)
# Silme yaptığımız zaman veri setindeki diğer değişkenlerdeki gözlem değerlerinide silmiş oluyoruz veri kaybediyoruz. Böyle zamanlarda baskılama yöntemide kullanılabilir.
# Nasıl çalışır? Belirlenen eşik değeri üzerindeki değerler eşik değeri ile değiştirilir.
###################

low, up = outlier_thresholds(df, "Fare")

# Aykırı değerleri seçelim
df[((df["Fare"] < low) | (df["Fare"] > up))]["Fare"]

df.loc[((df["Fare"] < low) | (df["Fare"] > up)), "Fare"]

df.loc[(df["Fare"] > up), "Fare"] = up

df.loc[(df["Fare"] < low), "Fare"] = low


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


df = load()
cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]

df.shape

for col in num_cols:
    print(col, check_outlier(df, col))

for col in num_cols:
    replace_with_thresholds(df, col)

for col in num_cols:
    print(col, check_outlier(df, col))

###################
# Recap
###################

df = load()
outlier_thresholds(df, "Age")
check_outlier(df, "Age")
grab_outliers(df, "Age", index=True)

remove_outlier(df, "Age").shape
replace_with_thresholds(df, "Age")
check_outlier(df, "Age")

#############################################
# Çok Değişkenli Aykırı Değer Analizi: Local Outlier Factor
#############################################

# 17, 3

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()  #Eksik değerleri drop edelim
df.head()
df.shape
for col in df.columns:
    print(col, check_outlier(df, col))

# Carat değlşkeninde kaçtane outlier var bakalım
low, up = outlier_thresholds(df, "carat")

# Kaç tane aykırı değer var
df[((df["carat"] < low) | (df["carat"] > up))].shape

low, up = outlier_thresholds(df, "depth")

df[((df["depth"] < low) | (df["depth"] > up))].shape

clf = LocalOutlierFactor(n_neighbors=20)  # Komşuluk sayısı ön tanımlı 20
clf.fit_predict(df)

df_scores = clf.negative_outlier_factor_
type(df_scores)
df_scores[0:5]
# df_scores = -df_scores  # Negatiflikten kurtulmak için - ile işleme aldık
np.sort(df_scores)[0:5]

# NOT : Daha negatif değerler, daha büyük olasılıkla aykırı değerleri işaret eder
# Elbow metodu : Noktaların her K değerine göre küme merkezine uzaklıklarının karesi toplamı hesaplanmaktadır
scores = pd.DataFrame(np.sort(df_scores))
scores.plot(stacked=True, xlim=[0, 50], style='.-')
plt.show()

th = np.sort(df_scores)[3]

df[df_scores < th]
# LOF sonrası kaç aykırı değer var bir bakalım.
df[df_scores < th].shape

df.describe([0.01, 0.05, 0.75, 0.90, 0.99]).T

df[df_scores < th].index

df[df_scores < th].drop(axis=0, labels=df[df_scores < th].index)

#############################################
# Missing Values (Eksik Değerler)
#############################################

#############################################
# Eksik Değerlerin Yakalanması
#############################################

df = load()
df.head()

# eksik gozlem var mı yok mu sorgusu
df.isnull().values.any()

# degiskenlerdeki eksik deger sayisi
df.isnull().sum()

# degiskenlerdeki tam deger sayisi
df.notnull().sum()

# veri setindeki toplam eksik deger sayisi
df.isnull().sum().sum()

# en az bir tane eksik degere sahip olan gözlem birimleri
df[df.isnull().any(axis=1)]

# tam olan gözlem birimleri
df[df.notnull().all(axis=1)]

# Azalan şekilde sıralamak
df.isnull().sum().sort_values(ascending=False)

(df.isnull().sum() / df.shape[0] * 100).sort_values(ascending=False)

# Eksik değere sahip olan değişkenlere ulaşalım
na_cols = [col for col in df.columns if df[col].isnull().sum() > 0]


def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]

    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")

    if na_name:
        return na_columns


missing_values_table(df)

missing_values_table(df, True)

#############################################
# Eksik Değer Problemini Çözme
#############################################

missing_values_table(df)

###################
# Çözüm 1: Hızlıca silmek
###################
df.dropna().shape

###################
# Çözüm 2: Basit Atama Yöntemleri ile Doldurmak
###################

df["Age"].fillna(df["Age"].mean()).isnull().sum()
df["Age"].fillna(df["Age"].median()).isnull().sum()
df["Age"].fillna(0).isnull().sum()

# df.apply(lambda x: x.fillna(x.mean()), axis=0) # Hata veriri çünkü kategork değişkenlerde vardır.
# boş değerleri ortlaam ile doldurmal
df.apply(lambda x: x.fillna(x.mean()) if x.dtype != "O" else x, axis=0).head()

dff = df.apply(lambda x: x.fillna(x.mean()) if x.dtype != "O" else x, axis=0)

dff.isnull().sum().sort_values(ascending=False)
#  Kategorik değişkenlerdeki eksik değerleri doldurmak için mod kullanalım
df["Embarked"].isnull().sum()
df["Embarked"].fillna(df["Embarked"].mode()[0]).isnull().sum()

df["Embarked"].fillna("missing")

df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum()

###################
# Kategorik Değişken Kırılımında Değer Atama
###################

# Veris setinde cinsiyete göre grupla yaşa göre ortalamasını al
df.groupby("Sex")["Age"].mean()

df["Age"].mean()
# Cinsiyet kırılımında yaş değişkeninin boş değerlerini dolduralım. Yani kadınlar yaş ortalaması kadınlarda ki NaN değerlere erkeklerinki de erkeklere :)
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()

df.groupby("Sex")["Age"].mean()["female"]

df.loc[(df["Age"].isnull()) & (df["Sex"] == "female"), "Age"] = df.groupby("Sex")["Age"].mean()["female"]

df.loc[(df["Age"].isnull()) & (df["Sex"] == "male"), "Age"] = df.groupby("Sex")["Age"].mean()["male"]

df.isnull().sum()

#############################################
# Çözüm 3: Tahmine Dayalı Atama ile Doldurma
#############################################

df = load()

cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]
# One Hot Encoding yapmak için get_dummies metodu kullanıyoruz.
dff = pd.get_dummies(df[cat_cols + num_cols], drop_first=True)

dff.head()

# değişkenlerin standartlaştırılması
scaler = MinMaxScaler()  # Değerleri 1-0 arasında dönüştür
dff = pd.DataFrame(scaler.fit_transform(dff), columns=dff.columns)
dff.head()

# knn'in uygulanması.
from sklearn.impute import KNNImputer

# Bana arkadaşını söyle sana kim olduğunu söylüyüm :)
imputer = KNNImputer(n_neighbors=5)
dff = pd.DataFrame(imputer.fit_transform(dff), columns=dff.columns)
dff.head()
9
# scaler işemini geriye dönüştürme
dff = pd.DataFrame(scaler.inverse_transform(dff), columns=dff.columns)

df["age_imputed_knn"] = dff[["Age"]]

#  Eksik değerler yerine hangi değerlerin atandığını gösterelim
df.loc[df["Age"].isnull(), ["Age", "age_imputed_knn"]]
df.loc[df["Age"].isnull()]

###################
# Recap
###################

df = load()
# missing table
missing_values_table(df)
# sayısal değişkenleri direk median ile oldurma
df.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0).isnull().sum()
# kategorik değişkenleri mode ile doldurma
df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum()
# kategorik değişken kırılımında sayısal değişkenleri doldurmak
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()
# Tahmine Dayalı Atama ile Doldurma


#############################################
# Gelişmiş Analizler
# ============================================
# Eksik Veri Yapısının İncelenmesi
###################
# msno kütüphanesinin bar fonk. ile eksik verieri bar grafiğinde gösterelim.
msno.bar(df)
plt.show()
#  matrix fonk ile eksik verilerin  dağılımını ve kalıplarıı keşfetmek için kullanılır. Mesela başka değişkenler ile benzerliklerine bakılabilir.
msno.matrix(df)
plt.show()
# Isı haritası
msno.heatmap(df)
plt.show()


###################
# Eksik Değerlerin Bağımlı Değişken ile İlişkisinin İncelenmesi
###################
# eksik değerler ve oranlarına bakalım
missing_values_table(df, True)
na_cols = missing_values_table(df, True)


def missing_vs_target(dataframe, target, na_columns):
    temp_df = dataframe.copy()

    for col in na_columns:
        temp_df[col + '_NA_FLAG'] = np.where(temp_df[col].isnull(), 1, 0)

    na_flags = temp_df.loc[:, temp_df.columns.str.contains("_NA_")].columns

    for col in na_flags:
        print(pd.DataFrame({"TARGET_MEAN": temp_df.groupby(col)[target].mean(),
                            "Count": temp_df.groupby(col)[target].count()}), end="\n\n\n")


# Survived değişkeni ile eksik değerler bulunan değişkenleri karşılaştırıyoruz
missing_vs_target(df, "Survived", na_cols)

###################
# Recap
###################

df = load()
na_cols = missing_values_table(df, True)
# sayısal değişkenleri direk median ile oldurma
df.apply(lambda x: x.fillna(x.median()) if x.dtype != "O" else x, axis=0).isnull().sum()
# kategorik değişkenleri mode ile doldurma
df.apply(lambda x: x.fillna(x.mode()[0]) if (x.dtype == "O" and len(x.unique()) <= 10) else x, axis=0).isnull().sum()
# kategorik değişken kırılımında sayısal değişkenleri doldurmak
df["Age"].fillna(df.groupby("Sex")["Age"].transform("mean")).isnull().sum()
# Tahmine Dayalı Atama ile Doldurma
missing_vs_target(df, "Survived", na_cols)

#############################################
# 3. Encoding (Label Encoding, One-Hot Encoding, Rare Encoding)
#############################################

#############################################
# Label Encoding & Binary Encoding
#############################################

df = load()
df.head()
df["Sex"].head()

le = LabelEncoder()
#  Alfabetik olarak encode edilir . Female 0, Male 1
le.fit_transform(df["Sex"])[0:5]
# Hangisine 0 hangisine 1 verilmiş bakalım
le.inverse_transform([0, 1])


def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe


df = load()
#   İki sınıflı kategorik değişkenleri bulalım
binary_cols = [col for col in df.columns if df[col].dtype not in ["int64", "float64"]
               and df[col].nunique() == 2]

for col in binary_cols:
    label_encoder(df, col)

df.head()

df = load_application_train()
df.shape

binary_cols = [col for col in df.columns if df[col].dtype not in ["int64", "float64"]
               and df[col].nunique() == 2]

df[binary_cols].head()

# NOT : Veri setinde NaN kısımlar var. Encode işlemi yapınca 2 ile dolduruldu. Bunun farkında olmak gerek.
for col in binary_cols:
    label_encoder(df, col)

df = load()
df["Embarked"].value_counts()
# Benzersiz değerlerin sayısı
df["Embarked"].nunique()
#  Benzersiz değerler ve nan değerlerde ifade edilir.
len(df["Embarked"].unique())

#############################################
# One-Hot Encoding
#############################################

df = load()
df.head()
df["Embarked"].value_counts()

pd.get_dummies(df, columns=["Embarked"]).head()
# Dummy değişken tuzağına düşmemek için drop - first yapalım. Multicollinearity
pd.get_dummies(df, columns=["Embarked"], drop_first=True).head()
# Eksik değerlerde bir sınıf olarak gelsin istersek.
pd.get_dummies(df, columns=["Embarked"], dummy_na=True).head()
# One - Hot ve Label Encoder bir arada yapalım
pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True).head()


def one_hot_encoder(dataframe, categorical_cols, drop_first=True):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe


df = load()

# cat_cols, num_cols, cat_but_car = grab_col_names(df)

# 2'den büyük ve 10' dan küçükse
ohe_cols = [col for col in df.columns if 10 >= df[col].nunique() > 2]

one_hot_encoder(df, ohe_cols).head()

df.head()

#############################################
# Rare Encoding
#############################################

# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
# 3. Rare encoder yazacağız.

###################
# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
###################

df = load_application_train()
df["NAME_EDUCATION_TYPE"].value_counts()

cat_cols, num_cols, cat_but_car = grab_col_names(df)


# Kategorik değişkenleri ve bu değişkenlerin sınıflarının oranlarını getiren bir fonk. yazalım.
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


for col in cat_cols:
    cat_summary(df, col)

###################
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
###################

df["NAME_INCOME_TYPE"].value_counts()

df.groupby("NAME_INCOME_TYPE")["TARGET"].mean()


def rare_analyser(dataframe, target, cat_cols):
    for col in cat_cols:
        print(col, ":", len(dataframe[col].value_counts()))
        print(pd.DataFrame({"COUNT": dataframe[col].value_counts(),
                            "RATIO": dataframe[col].value_counts() / len(dataframe),
                            "TARGET_MEAN": dataframe.groupby(col)[target].mean()}), end="\n\n\n")


rare_analyser(df, "TARGET", cat_cols)


#############################################
# 3. Rare encoder'ın yazılması.
#############################################

def rare_encoder(dataframe, rare_perc):
    temp_df = dataframe.copy()

    rare_columns = [col for col in temp_df.columns if temp_df[col].dtypes == 'O'
                    and (temp_df[col].value_counts() / len(temp_df) < rare_perc).any(axis=None)]

    for var in rare_columns:
        # Değişkenin tüm df deki oranını hesaplayalım
        tmp = temp_df[var].value_counts() / len(temp_df)
        # Verilen yüzdelik değerin altında olan değerleri bulalım.
        rare_labels = tmp[tmp < rare_perc].index
        # DF deki nadir olan değerleri Rare olarak sınıflayıp olmayanları olduğu gibi bırakalım
        temp_df[var] = np.where(temp_df[var].isin(rare_labels), 'Rare', temp_df[var])

    return temp_df


new_df = rare_encoder(df, 0.01)

rare_analyser(new_df, "TARGET", cat_cols)

df["OCCUPATION_TYPE"].value_counts()

#############################################
# Feature Scaling (Özellik Ölçeklendirme)
#############################################

###################
# StandardScaler: Klasik standartlaştırma(Normalleştirme). Ortalamayı çıkar, standart sapmaya böl. z = (x - u) / s
###################

df = load()
ss = StandardScaler()
df["Age_standard_scaler"] = ss.fit_transform(df[["Age"]])
df.head()

###################
# RobustScaler: Medyanı çıkar iqr'a böl.
###################

rs = RobustScaler()
df["Age_robuts_scaler"] = rs.fit_transform(df[["Age"]])
df.describe().T

###################
# MinMaxScaler: Verilen 2 değer arasında değişken dönüşümü
###################

# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min

mms = MinMaxScaler()
df["Age_min_max_scaler"] = mms.fit_transform(df[["Age"]])
df.describe().T

df.head()

age_cols = [col for col in df.columns if "Age" in col]


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in age_cols:
    num_summary(df, col, plot=True)

###################
# Numeric to Categorical: Sayısal Değişkenleri Kateorik Değişkenlere Çevirme
# Binning
###################

df["Age_qcut"] = pd.qcut(df['Age'], 5)

#############################################
# Feature Extraction (Özellik Çıkarımı)
#############################################

#############################################
# Binary Features: Flag, Bool, True-False
#############################################
#  Survived bağımlı değişken
df = load()
df.head()
# NaN olan kısımları 0 dolulara 1 yazalım
df["NEW_CABIN_BOOL"] = df["Cabin"].notnull().astype('int')

# Kabin değeri olan yolcuların haytta kalma olasılığı daha yüksek.
df.groupby("NEW_CABIN_BOOL").agg({"Survived": "mean"})

# İki grubun oranlarının kıyaslaması testi yapalım
from statsmodels.stats.proportion import proportions_ztest

# proportions_ztest(başarısayısı,gözlem sayısı)
test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].sum(),
                                             df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].sum()],

                                      nobs=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].shape[0],
                                            df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].shape[0]])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Akrabalık ilişkisinin hayatta kalmaya etkisi için feature oluşturacağız.
df.loc[((df['SibSp'] + df['Parch']) > 0), "NEW_IS_ALONE"] = "NO"
df.loc[((df['SibSp'] + df['Parch']) == 0), "NEW_IS_ALONE"] = "YES"

df.groupby("NEW_IS_ALONE").agg({"Survived": "mean"})

test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].sum(),
                                             df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].sum()],

                                      nobs=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].shape[0],
                                            df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].shape[0]])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#############################################
# Text'ler Üzerinden Özellik Türetmek
#############################################

df.head()

###################
# Letter Count - Harfleri sayalım(Boşluklarda dahil)
###################
df["NEW_NAME_COUNT"] = df["Name"].str.len()

###################
# Word Count
###################
df["NEW_NAME_WORD_COUNT"] = df["Name"].apply(lambda x: len(str(x).split(" ")))

###################
# Özel Yapıları Yakalamak
###################

df["NEW_NAME_DR"] = df["Name"].apply(lambda x: len([x for x in x.split() if x.startswith("Dr")]))

df.groupby("NEW_NAME_DR").agg({"Survived": ["mean", "count"]})

###################
# Regex ile Değişken Türetmek
###################

df.head()
# Tittle'ları ayıralım
df['NEW_TITLE'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

df[["NEW_TITLE", "Survived", "Age"]].groupby(["NEW_TITLE"]).agg({"Survived": "mean", "Age": ["count", "mean"]})

#############################################
# Date Değişkenleri Üretmek
#############################################

dff = pd.read_csv("Feature_Engineering/datasets/course_reviews.csv")
dff.head()
dff.info()

dff['Timestamp'] = pd.to_datetime(dff["Timestamp"], format="%Y-%m-%d %H:%M:%S")

# year
dff['year'] = dff['Timestamp'].dt.year

# month
dff['month'] = dff['Timestamp'].dt.month

# year diff
dff['year_diff'] = date.today().year - dff['Timestamp'].dt.year

# month diff (iki tarih arasındaki ay farkı): yıl farkı + ay farkı
dff['month_diff'] = (date.today().year - dff['Timestamp'].dt.year) * 12 + date.today().month - dff['Timestamp'].dt.month

# day name
dff['day_name'] = dff['Timestamp'].dt.day_name()

dff.head()

# date


#############################################
# Feature Interactions (Özellik Etkileşimleri) - Değişkenlerin birbirleri ile iletişime girmesi demektir.
#############################################
df = load()
df.head()

df["NEW_AGE_PCLASS"] = df["Age"] * df["Pclass"]

df["NEW_FAMILY_SIZE"] = df["SibSp"] + df["Parch"] + 1

df.loc[(df['Sex'] == 'male') & (df['Age'] <= 21), 'NEW_SEX_CAT'] = 'youngmale'

df.loc[(df['Sex'] == 'male') & (df['Age'] > 21) & (df['Age'] < 50), 'NEW_SEX_CAT'] = 'maturemale'

df.loc[(df['Sex'] == 'male') & (df['Age'] >= 50), 'NEW_SEX_CAT'] = 'seniormale'

df.loc[(df['Sex'] == 'female') & (df['Age'] <= 21), 'NEW_SEX_CAT'] = 'youngfemale'

df.loc[(df['Sex'] == 'female') & (df['Age'] > 21) & (df['Age'] < 50), 'NEW_SEX_CAT'] = 'maturefemale'

df.loc[(df['Sex'] == 'female') & (df['Age'] >= 50), 'NEW_SEX_CAT'] = 'seniorfemale'

df.head()

df.groupby("NEW_SEX_CAT")["Survived"].mean()
