###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
print(type(x))

y = 3.2
print(type(y))

z = 8j + 18
print(type(z))

a = "Hello World"
print(type(a))

b = True
print(type(b))

c = 23 < 22
print(type(c))

l = [1, 2, 3, 4]
print(type(l))

d = {"Name": "Berna",
     "Age": 27,
     "Adress": "İstanbul"}

print(type(d))

t = ("Machine Learning", "Data Science")
print(type(t))

s = {"python", "Machine Learning", "Data Science"}
print(type(s))

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
clean_text = text.upper().replace(".", " ").replace(",", " ")
clean_text = ' '.join(clean_text.split())  # Ardışık boşlukları temizler
print(clean_text.split(" "))

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

#Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(lst))

#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print(lst[0])
print(lst[10])

#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
new_lst = lst[0:4]
print(new_lst)
#Adım 4: Sekizinci indeksteki elemanı siliniz.
print(lst.pop(8))
print(lst)
#Adım 5: Yeni bir eleman ekleyiniz.
lst.append("ML")
print(lst)
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz
lst.insert(8, "N")
print(lst)

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

#Adım 1: Key değerlerine erişiniz.
print(dict.keys())
#Adım 2: Value'lara erişiniz.
print(dict.values())
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
print(dict.update({"Daisy": ["England", 13]}))
print(dict)
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
print(dict)
#Adım 5: Antonio'yu dictionary'den siliniz.
# 'Antonio' anahtarını içeren öğeyi sil
del dict['Antonio']

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []
def even_odd_lıst(listnumber):
    for number in listnumber:
        even_list.append(number) if number % 2 == 0 else odd_list.append(number)
    return even_list, odd_list


even_list1, odd_list1 = even_odd_lıst(l)


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

# ÇIKTI
# Mühendislik Fakültesi 1. Öğrenci : Ali
# Mühendislik Fakültesi 2. Öğrenci : Veli
# Mühendislik Fakültesi 3. Öğrenci : Ayşe
# Tıp Fakültesi 1. Öğrenci : Talat
# Tıp Fakültesi 2. Öğrenci : Zeynep
# Tıp Fakültesi 3. Öğrenci : Ece
###############################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
derece = 0
for index, student in enumerate(ogrenciler, 1):
    if index <= 3:
        print(f"Mühendislik Fakültesi {index}. Öğrenci : {student}")
    else:
        derece += 1
        print(f"Tıp Fakültesi {derece}. Öğrenci : {student}")


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

new_lst = list(zip(ders_kodu, kredi, kontenjan))
for item in new_lst:
    print(f"Kredisi {item[1]} olan {item[0]} kodlu dersin kontenjanı {item[2]} kişidir.")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def dif_issuper_set(set1, set2):
    # kapsayıp kapsamadığı kontrol edildi.
    if set1.issuperset(set2):
        # ortak elemanlar
        print(set1.intersection(set2))
    else:
        # farklı elemanları bulduk
        print(set2.difference(set1))


dif_issuper_set(kume1, kume2)