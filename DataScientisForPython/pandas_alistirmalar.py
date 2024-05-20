##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df = sns.load_dataset("titanic")
df.head()

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################
df["sex"].value_counts()
# Ekrana çıktı vermek istersek value_counts().items() bize dict yapısı sunar.
for sex, count in df["sex"].value_counts().items():
    print(f"{sex}: {count}")

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
uniq_counts = df.nunique()
# for col in df.columns:
#     print(f" {col} : {df[col].unique()}")

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################
print(f"pclass : {df['pclass'].unique()}")
# for col in df.columns:
#     print(f" {col} : {df[col].unique()}")


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################
unique_counts = df[['parch', 'pclass']].nunique()
print(f"pclass : {df['pclass'].nunique()}")
print(f"parch : {df['parch'].nunique()}")

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################
old_type = df["embarked"].dtypes
df["embarked"] = df["embarked"].astype('category')
df.info()

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################
df.head()
embarked_c_passengers = df.loc[df['embarked'] == 'C']

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################
embarked_c_q_passengers = df.loc[df['embarked'] != 'S']

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################
df_temp = df.loc[(df["age"] < 30) & (df["sex"] == "female")]
df_temp.head()

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################
df_temp = df.loc[(df["fare"] > 500) | (df["age"] > 70)]
df_temp.head()

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################
df.isnull().sum()
null_age = df['age'].isnull()
# Embarked değeri boş olan kayıtlları getir.
null_embarked = df[df['embarked'].isnull()]

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################
df.drop("who", axis=1).head()
# Birden çok değişken silmek çin liste gönderebiliriz.
# df.drop(col_names, axis=1).head()


#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

# En çok tekrar eden değeri bulmak (mode)
mode_deck = df['deck'].mode()[0]
# Bir Seri üzerinde idxmax() kullanarak en büyük değere sahip olan dizin etiketini
most_common_value = df['deck'].value_counts().idxmax()

# Boş değerlere mode değerini atamak
df.loc[df["deck"].isnull(), 'deck'] = mode_deck
# II . YOL
df['deck'].fillna(mode_deck, inplace=True)

check_null_deck = df[df['deck'].isnull()]

df = sns.load_dataset("titanic")
df.head()

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################
median_age = df["age"].median()
check_null_age = df['age'].isnull().sum()
df['age'].fillna(median_age, inplace=True)

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
df = sns.load_dataset("titanic")
# Pclass ve Sex kolonlarına göre gruplama yapalım daha sonra survived değişkenine agg fonk. uygulayalım.
df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "mean", 'count']})

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################
df = sns.load_dataset("titanic")


def age_to_binary(age):
    result = 0 if age > 30 else 1
    return result


df['age_flag'] = df['age'].apply(age_to_binary)
df['age_flag'] = df['age'].apply(lambda x: 0 if x >= 30 else 1)
df.head()

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################
df = sns.load_dataset("tips")
df.head()
df.info()

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################
df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################
lunch_female_df = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
lunch_female_df.groupby("day",observed=True).agg({"total_bill": ["sum", "min", "max", "mean"],
                                                  "tip": ["sum", "min", "max", "mean"]})

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################
df.head()
df[(df["size"] < 3) & (df["total_bill"] > 10)]["total_bill"].mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################
df = sns.load_dataset("tips")
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################
df_temp = df.sort_values(by="total_bill_tip_sum",ascending=False).head(30)