#####################################################
# Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Eda)
####################################################

# 1. Genel Resim
###########################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()


def check_df(dataframe, head=5):
    print("############### Shape  ###############")
    print(dataframe.shape)
    print("############### Types  ###############")
    print(dataframe.dtypes)
    print("############### Head  ###############")
    print(dataframe.head(head))
    print("############### Tail  ###############")
    print(dataframe.tail(head))
    print("############### NA  ###############")
    print(dataframe.isnull().sum())
    print("############### Quantiles  ###############")
    print(dataframe.describe([0, 0.85, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("tips")
check_df(df)
df = sns.load_dataset("flights")
check_df(df)

# 2. Kategorik Değiişken Analizi (Analysis of Categorical Variables)
####################################################################
df = sns.load_dataset("titanic")
df.head()
# Tek bir değişkene göre
df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()
df["age"].nunique()
df["fare"].nunique()

# Kategorik değişkenleri seçme : bool,category ve object tipleri kategori tipindedir.
# Survived - sinsirella int dır ama kategorikdir.

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# int ve float değişkenlerde eşssiz class sayısını(nunique) bul
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

#  Kategorik gibi duran fakat kardenel olan değişkenlervarsa kategorik kolonlardan çıkarılması gerek
cat_cols = [col for col in cat_cols if col not in cat_but_car]

# Kategorik olarak bulduğumuz değişkenlerin sınıf sayısı
df[cat_cols].nunique()

# Veri setindeki sayısal değişkenler
num_col = [col for col in df.columns if col not in cat_cols]

df["survived"].value_counts()  # hangi sınıftan kaçar tane
100 * df["survived"].value_counts() / len(df)  # sınıflarının yüzdelik bilgisi


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)


# cat_summary fonksiyonuna grafik özelliği ekleme
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == 'bool':
        print("sdfskfsgsgllllsg")
    else:
        cat_summary(df, col, plot=True)

# bool değişkeni değiştirmek istiyoruz. Yani grafik çizebilmek için uyygun hale getiriyoruz.
df = sns.load_dataset("titanic")

df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == 'bool':
        df[col] = df["adult_male"].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


# Bool değişkenler için tip sorgulmasını fonk. içerisine almak.
def cat_summary(dataframe, col_name, plot=False):
    if dataframe[col_name].dtypes == 'bool':
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


cat_summary(df, 'adult_male', plot=True)

# Sayısal Değişken Analizi (Analysis of Numerical Variables)
##############################################################

df = sns.load_dataset("titanic")
df.head()

df[["age", "fare"]].describe().T

# Veri setinden numeric değerleri nasıl seçeriz?
num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

# num_cols da olup cat_cols da olmayanları seçelim
num_cols = [col for col in num_cols if col not in cat_cols]


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, True)

# Değişkenlerin Yakalanması ve İşlemlerin Güncelleştirilmesi
############################################################
df = sns.load_dataset("titanic")
df.head()
df.info()


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki, kategorik, numeric ve kategorik fakat kardinal değişkenlerin isimlerini verir
    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th : int,float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int,float
        kategorik fakat kardinal olan değişkenler için sınıf eşik değeri
    Returns
    -------
    cat_cols : list
        Kategorik değişken listesi
    num_cols : list
        Numeric değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + car_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde

    """

    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    # int ve float değişkenlerde eşssiz class sayısını(nunique) bul
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat

    #  Kategorik gibi duran fakat kardenel olan değişkenlervarsa kategorik kolonlardan çıkarılması gerek
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Veri setinden numeric değerleri nasıl seçeriz?
    num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

    # num_cols da olup cat_cols da olmayanları seçelim
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observation: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


help(grab_col_names)

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex", plot=True)

for col in cat_cols:
    cat_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)

# BONUS
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == 'bool':
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

# Hedef Değişkenlerin Analizi (Analysis of Target Variable)
############################################################
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == 'bool':
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

df.head()
df["survived"].value_counts()
cat_summary(df, "survived")

# Hedef Değişkenin Kategorik Değişkenler ile Analizi
####################################################

df.groupby("sex")["survived"].mean()


def target_summary_wit_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col, observed=True)[target].mean()}))


target_summary_wit_cat(df, "survived", "sex")

target_summary_wit_cat(df, "survived", "pclass")

for col in cat_cols:
    # print(f" {col} {df[col].dtypes}")
    target_summary_wit_cat(df, "survived", col)

# Hedef Değişkenin Sayısal Değişkenler ile Analizi
####################################################

# Bağımlı değişken groupby içerisine
df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age": "mean"})


def target_summary_wit_num(dataframe, target, numeric_col):
    print(pd.DataFrame(dataframe.groupby(target, observed=True).agg({"age": "mean"})))


target_summary_wit_num(df, "survived", "age")

for col in num_cols:
    target_summary_wit_num(df, "survived", col)