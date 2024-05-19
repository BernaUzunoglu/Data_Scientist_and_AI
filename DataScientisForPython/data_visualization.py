#############################################
# Veri Görselleştirme : Matplotlib & Seaborn
############################################
import numpy as np
# MATPOLTLIB

# Kategorik değişkenler : Sütun grafik, countplot
# Sayısal değişken : hist, boxplot

####################################
# Kategorik Değişken Görselleştirme
###################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show()  # Grafiği ekrana yazdırma

####################################
# Sayısal Değişken Görselleştirme
###################################
# Histogram ve boxplot grafik sayısal değişkenlerin dağılım ve frekans bilgisi ve dağılama göre aykırı veriyi görselleştirir.
plt.hist(df["age"])  # Sayısal değişkenlerin dağılımını verir. 0-10 arasında kaç kişi var vs.
plt.show()

plt.boxplot(df["fare"])  # Kutu grafik ile genel dağılımın dışındaki verileri yakalayabiliriz. Aykırı veriler gibi
plt.show()


###########################
# Matplotlib ' in Özellikleri
###########################
# PLOT
x = np.array([1, 8])
y = np.array([0, 150])
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

# MARKER
y = np.array([13, 28, 11, 100])
plt.plot(y, marker='*')
plt.show()

markers = {'o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h'}


# LINE
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle='dashed', color="r")
# plt.plot(y, linestyle='dashdot')
# plt.plot(y, linestyle='dotted')
plt.show()

# MULTIPLE LINE
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# LABEL
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık")

# X ekseni isimlendirme
plt.xlabel("X ekseni isimlendirme")
plt.ylabel("Y ekseni isimlendirme")
plt.grid()
plt.show()


# SUBPLOTS
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)

# 3 grafiği bir satır 3 sütun olarak konumlamak.

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

#######################################
# SEABORN
#######################################

# SEABORN ile Kategorik Değişkenleri Görselleştirme
df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x='sex', data=df)
plt.show()

# matplotlib ile uzun yoldan :)
df['sex'].value_counts().plot(kind='bar')
plt.show()

# SEABORN ile Sayısal Değişkenleri Görselleştirme
sns.boxplot(x=df['total_bill'])
plt.show()

df['total_bill'].hist()
plt.show()