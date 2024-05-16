# Python ile Veri Analizi (Data Analysis With Python)
#########################
# - Numpy
# - Pandas
# - Veri Görselleştirme : Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi(Advanced Functional Exploratory Data Analysis)
#########################
# NUMPY
#########################

# Neden Numpy?
# 1)Hız
# 2) Yüksek seviyeden vektörel işlemler yapma imkanı sunar(Daha az çaba daha fazla iş)

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b  # daha az çaba daha fazla işlem.

# Numpy arrayleri oluşturmak.(Creating Numpy Arrays)
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))  # ortalaması 10 olan stnd sap.4 olan 3' e 4'lük matris normal dağılımlı sayılar

###############################################################

# Numpy Array Özellikleri(Attributes of Numpy Arrays)
# ndim (n dimention): boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
dimention = a.ndim  # boyut sayısı verir
boyut = a.shape  # (5,) tek boutlu ve 5 elemanlı , iki boyutlu olsa idi her boyuttaki eleman sayısı gelecekti.
top_ele = a.size  # 5 değeri gelir.
veri_tip = a.dtype

###############################################################

# Yeniden Şekillendirme(Reshaping)
# Elimizdeki bir numpy arrayinin boyutunu değiştirmek istediğimizde reshape metodu kullanılır.
np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

# NOT : Eleman sayısı ile matrisin boyutunda  olmalı mesela 10 elemanlı bir array 3x3 matrise olmaz 9 elelmanlı olması gerek
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

# np.random.randint(1, 10, size=8).reshape(3, 3)  #Hata verir.

###############################################################

# Index Seçimi (Index Selection)

a = np.random.randint(10, size=10)
selec = a[0]
selec1 = a[0:5]
selec2 = a[0] = 999

m = np.random.randint(10, size=(3, 5))
# m[satır,sütun]
selec3 = m[0, 0]
selec4 = m[1, 1]
selec5 = m[2, 3]
m[2, 3] = 999
m[0, 0] = 12.4  # float bir değer girilince sadece int kısmını aldı.Çünkü numpy tektiip veri tutar.

butun_satirlar = m[:, 0]
butun_sutunlar = m[0, :]
hem_satir_hem_sutun = m[0:2, 0:3]

###############################################################

# Fancy Index
# Bir numpy arrayine liste girdiğimiz vakit (index numarası veya true false içeriyor olabilir) kolay bir şekilde seçim imkanı sunar.
v = np.arange(0, 30, 3)  # 0 'dan 30 kadar üçer üçer artacak
v[1]
v[4]

catch = [1, 2, 3]
v[catch]

###############################################################

# Numpy'da Koşullu İşlemler () Comditions on Numpy

v = np.array([1, 2, 3, 4, 5])
# 3' den küçük olanları bulma
ab = []

for i in v:
    if i < 3:
        ab.append(i)

var1 = v < 3
var2 = v[v < 3]
var3 = v[v > 3]
var4 = v[v != 3]
var5 = v[v == 3]
var6 = v[v >= 3]

# Matematiksel İşlemler (Mathematical Operations)
v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)  # Çıkarma
np.add(v, 1)  # Toplama
np.mean(v)  # Ort
np.sum(v)  # Toplam alma
np.min(v)  # Min
np.max(v)  # Max
np.var(v)  # Varyant

#########################################
# Numpy ile İki Bilinmeyenli Denklem Çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])  #Denklemllerin başkat sayıları
b = np.array([12, 10])
np.linalg.solve(a, b)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-4:-2])

array = np.array([1, 2, 3, 4, 5, 6, 7])
filter_array = array % 2 == 0
new_array = array[filter_array]
print(new_array)