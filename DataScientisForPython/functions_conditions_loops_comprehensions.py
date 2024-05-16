# Fonksiyon Tanımlama

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonk tanımlayalım.
def summer(arg1, arg2):  #  argümaların sırasıda önemli
    print(arg1 + arg2)


summer(7, 8)
summer(arg2=8, arg1=7)


# DOCSTRING : Kullanıcılara herkesin anlayabileceği bir dille bilgi notu ekleme yolu.
def summer(arg1, arg2):
    """
    Sum of two numbers
    Parameters / Args
    ----------
    arg1 : int,float
    arg2 : int,float

    Returns
    -------
    int,float
    """
    print(arg1 + arg2)


summer(1, 3)


# Fonksiyonların Statement/Body Bölümü

# def function_name(parameters/arguments):
#      statements(function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# Girilen değerleri bir liste içinde saklayacak fonksiyon.
list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


###########################################
# Ön Tanımlı argümanlar / parametreler : Fonk. oluştururken bazı parametreler ön tanımlı, değer atanarak tanımlanabilir. Kullanım amaçlarına göre değişir.
##########################################
def divide(a, b):
    print(a / b)


divide(1, 2)


def say_hi(string="Merhaba Ben"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()
say_hi("Berna")


# Ne zaman fonksiyon yazma ihtiyacımız olur?
# warm, moisture, charge
# DRY prensibi derki kendini tekrar etme. Tekrar eden görevler söz konusu olduğunda fonk. yazmak gerekir.

def calculate(warm, moisture, charge):
    print((warm + moisture) / charge)


calculate(98, 12, 78)


##########################################
# Return : Fonksiyon Çıktılarını Girdi Olarak Kullanmak
##########################################

def calculate(warm, moisture, charge):
    c = (warm + moisture) / charge
    return c


calculate(98, 12, 78) * 10


# birden çok çıktılı return fonksiyon
def calculate(warm, moisture, charge):
    warm = warm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (warm + moisture) / charge

    return warm, moisture, charge, output


warm1, moisture1, charge1, output = calculate(98, 12, 78)


##########################################
# Fonksiyon içerisinden fonksiyon çağırmak
##########################################

def calculate(warm, moisture, charge):
    c = int((warm + moisture) / charge)
    return c


calculate(98, 12, 78)


def standardization(x, p):
    return x * 10 / 100 * p * p


standardization(45, 1)


def all_calcuulation(warm, moisture, charge, p):
    x = calculate(warm, moisture, charge)
    b = standardization(x, p)
    print(b * 10)


all_calcuulation(1, 3, 5, 12)

##########################################
# Local ve global değişkenler (Local & Global Variables)
##########################################

# list_store1 global bir scope da
list_store1 = [1, 2]


def add_element(a, b):
    # c Local bir scope local değişken.
    c = a * b
    list_store1.append(c)
    print(list_store1)


add_element(1, 9)

############################
# Koşullar
############################

# if
if 1 == 1:
    print("something")


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")


number_check(10)
number_check(12)


########################
# elif
#########################

def number_check(number):
    if number > 10:
        print("Greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")


number_check(8)
number_check(12)

########################
# Döngüler(Loops)
#########################
# for loop
students = ["John", "Mark", "Vanessa", "Mariam"]
# students listesinin elemanlarına ulaşma
# students[0]
# students[1]
# students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(int(salary * 20 / 100 + salary))

for salary in salaries:
    print(int(salary * 30 / 100 + salary))

for salary in salaries:
    print(int(salary * 50 / 100 + salary))


# işlem için fonksiyon yazalım.

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)
new_salary(2000, 30)

for salary in salaries:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 30))
    else:
        print(new_salary(salary, 40))

###########################
# Uygulama Mülakat Sorusu
###########################

# Amaç : Aşağıdaki şekilde string değiştiren fonksiyonu yazamak istiyoruz.
# before : "hi my name is john and i am learning python"
# before : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


for i in range(0, 5):
    print(i)


def change_str(string):
    new_string = ""
    for string_index in range(len(string)):
        print(string_index)
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    return new_string


new_str = change_str("hi my name is john and i am learning python")
print(new_str)


# Enumerate ile çözümü
def alternating(string):
    new_string = ""
    for i, letter in enumerate(string):
        new_string += letter.upper() if i % 2 == 0 else letter.lower()
    return new_string


new_str = alternating("hi my name is john and i am learning python")
print(new_str)

#########################
# break  continue  while
#########################

slry = [1000, 2000, 3000, 4000, 5000]

for item in slry:
    if item == 3000:
        break
    print(item)

for item in slry:
    if item == 3000:
        continue
    print(item)

# while
number = 1
while number < 5:
    print(number)
    number += 1

###############################
# Enumarate : otomatik counter / Indexer ile for loop
# iteratif uygulanabilir yapılar örneğin listeler üzerinde gezerken index bilgisinede erişilebilen yapılar.
#############################

students_list = ["Berna", "Banu", "Lina", "Mariam"]

for student in students_list:
    print(student)

for index, student in enumerate(students_list):
    print(index, student)

A = []
B = []
for index, student in enumerate(students_list):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

############################
# Uygulamam Mülakat Sorusu
#########################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students_list1 = ["Berna", "Banu", "Lina", "Emin", "Sevtap", "Hüsnü"]


# Çözüm Yöntemi I
def divide_students(student_list):
    even_student_list = []
    odd_student_list = []
    all_student_list = []
    for index, student in enumerate(student_list):
        odd_student_list.append(student) if index % 2 == 0 else even_student_list.append(student)
    all_student_list = [even_student_list, odd_student_list]
    return all_student_list


# Çözüm Yöntemi II
def divide_students1(student_list):
    all_student_list = [[], []]
    for index, student in enumerate(student_list):
        all_student_list[0].append(student) if index % 2 == 0 else all_student_list[1].append(student)
    return all_student_list


merge_list = divide_students1(students_list1)
print(merge_list)
print(merge_list[0])
print(merge_list[1])

##############################
# Zip : Elemanları eşlemek için kullanılır.Elemanları birleştirerek bir zip nesnesi oluşturur. Bu zip nesnesi, aynı indeksteki elemanları içeren bir grup tuple içerir.
#############################
students = ["Berna", "Turan", "Şamil", "Yakup"]
departments = ["Programming", "Algorithm", "Statistic", "Mathematics"]
ages = [26, 27, 28, 27]

list(zip(students, departments, ages))


# ÇIKTI [('Berna', 'Programming', 26), ('Turan', 'Algorithm', 27), ('Şamil', 'Statistic', 28), ('Yakup', 'Mathematics', 27)]

##############################
# Lambda, map, filter, reduce
# Lambda fonksiyonları, isimsiz (anonim) fonksiyonlardır ve genellikle tek satırda tanımlanır. Lambda ifadesi, Python'da fonksiyon tanımlamanın kısa bir yoludur.
############################

def summer(a, b):
    return a + b


summer(1, 3) * 9

new_sum = lambda a, b: a + b
new_sum(8, 7)

# map
# Sanki döngü yazmış gibi her elemana fonksiyon uygulanır.
# Python'da bir iterable'in (liste, demet, dize vb.) her öğesi üzerinde belirli bir işlemi uygulamak için kullanılır. Bu işlem, bir fonksiyonun her öğeye uygulanmasıdır.
maaslar = [1000, 2000, 3000, 4000, 5000]


def yeni_maas(x):
    return x * 20 / 100 + x


yeni_maas(1000)
list(map(yeni_maas, maaslar))

# Kullan at fonk. Yani atama işlemi yapmadan da kullanılabiliyor.
list(map(lambda x: x * 20 / 100 + x, maaslar))

list(map(lambda x: x ** 2, maaslar))

# Filter : Filtreleme işlemleri için kullanılır.

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE : İndirgemek demek
from functools import reduce

list_store2 = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store2)

############################
# COMPREHENSIONS
# Birden fazla satır ve kod ile yapılabilecek işlemleri kolayca istediğimiz çıktı veri yapısına göre tek bir satırda gerçekleştirme imkanı sağlayan yapılardır.
############################

# List Comprehensions
salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary1(x):
    return int(x * 20 / 100 + x)


for salary in salaries:
    print(new_salary1(salary))

null_list = []
for salary in salaries:
    null_list.append(new_salary1(salary))

null_list = []
for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary1(salary))
    else:
        null_list.append(new_salary1(salary * 2))

[new_salary1(salary * 2) if salary < 3000 else new_salary1(salary) for salary in salaries]

var = [salary * 2 for salary in salaries]
# Comprehensions yazarken eğer sadece if yazılacaksa if sağ tarafta kalır.
var1 = [salary * 2 for salary in salaries if salary < 3000]
# Comprehensions yazarken eğer sadece if ile else  yazılacaksa for sağ tarafta kalır.
var2 = [salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
var3 = [new_salary1(salary * 2) if salary < 3000 else new_salary1(salary * 0.2) for salary in salaries]

students = ["Berna", "Banu", "Esra", "Kevser"]
students_no = ["Esra", "Banu"]

student_list = [student.lower() if student in students_no else student.upper() for student in students]
# Öğrencilerde for ile gezdik yakaladığımız öğrenci istenmeyen öğrenci listesinde varsa küçük yoksa büyük harfe çevirdik.
student_list1 = [student.upper() if student not in students_no else student.lower() for student in students]

# Dict Comprehensions

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

dict1 = {k: v ** 2 for (k, v) in dictionary.items()}
dict2 = {k.upper(): v for (k, v) in dictionary.items()}
dict3 = {k.upper(): v * 2 for (k, v) in dictionary.items()}

###############################
# UYGULAMA - MÜLAKAT SORUSU
###############################
# Amaç : Çift sayıların karesi alınarak bir sözlüğe eklemek istenmektedir.
# Keyler orjinal değerler valueler ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}
for num in numbers:
    if num % 2 == 0:
        new_dict[num] = num ** 2
    # eğer listede çiftlerin alınması tek lerin direk yazılması istenseydi bu kodlar ile yapılacaktı.
    # else:
    #     new_dict[num] = num
new_dict1 = {n: n ** 2 for n in numbers if n % 2 == 0}

#############################
# List & Dict Comprehensions
############################

# Bir veri setindeki değişken isimlerini değiştirmek.
import seaborn as sns

df = sns.load_dataset("car_crashes")
columns_names = df.columns
df.info()

for col in df.columns:
    print(col.upper())

A = []
for col in df.columns:
    A.append(col.upper())
df.columns = A

# List Comprehension
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

# İçerisinde INS olanları getir
col1 = [col for col in df.columns if "INS" in col]

# İçerisinde INS geçenlerin başına FLAG ekle
col2 = ["FLAG_" + col for col in df.columns if "INS" in col]

# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
df.columns = ["FLAG_ " + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

#######################
# Mülakat Tadında
######################
# Amaç : key'i string , value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.

# Output:
# {'total': ['mean', 'min', 'max', 'sum'],
#  'speeding': ['mean', 'min', 'max', 'sum'],
#  'alcohol': ['mean', 'min', 'max', 'sum'],
#  'not_distracted': ['mean', 'min', 'max', 'sum'],
#  'no_previous': ['mean', 'min', 'max', 'sum'],
#  'ins_premium': ['mean', 'min', 'max', 'sum'],
#  'ins_losses': ['mean', 'min', 'max', 'sum']
#  }
df = sns.load_dataset("car_crashes")
df.info()

# Sayısal olan kolonları seçme işlemi
num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# Kısa yol
new_dictionary = {col: agg_list for col in num_cols}
df[num_cols].head()

# agg fonksiyonu eğer içerisine verilen sözlükte key değerleri col isimlerinde varsa value değerlerinde ki işlemleri otomatik olarak ekler.
df[num_cols].agg(new_dictionary)

liste = [1, 2, 3, 4, 5]
yeni_liste = [i for i in liste]
print(yeni_liste)

print([i * 2 for i in range(1, 5)])


def tek_mi(x):
    if x % 2 == 0:
        return False
    if x % 2 != 0:
        return True


tek_sayi = [i for i in range(1, 11) if tek_mi(i)]
print(tek_sayi)


eski_fiyat = {'süt': 1.02, 'kahve': 2.5, 'ekmek': 2.5}

dolar_tl = 0.76
yeni_fiyat = {item: value * dolar_tl for (item, value) in eski_fiyat.items()}
print(yeni_fiyat)


original_dict = {'ahmet': 38, 'mehmet': 48, 'ali': 57, 'veli': 33}

dict2 = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(dict2)

a = range(10)
type(a)