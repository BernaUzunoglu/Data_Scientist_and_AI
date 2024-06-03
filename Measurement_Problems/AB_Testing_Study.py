#####################################################
# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################
#  Bidding Yöntemlerinin : reklam teklif stratejilerini ifade eder
#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchase metriğine odaklanılmalıdır.


#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna Average Bidding uygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç

#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.


import itertools
import pandas as pd
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option("display.width", 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################
# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.
# Maximum Bidding kontrol grubuna uygulandı
ab_testing_kontrol = pd.read_excel("Measurement_Problems/datasets/ab_testing.xlsx", sheet_name="Control Group")
# Average Bidding
ab_testing_test = pd.read_excel("Measurement_Problems/datasets/ab_testing.xlsx", sheet_name="Test Group")

# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
def check_df(dataframe, head=5):
    print("############### Shape  ###############")
    print(dataframe.shape)
    print("############### Columns  ###############")
    print(dataframe.columns)
    print("############### Info  ###############")
    print(dataframe.info())
    print("############### Head  ###############")
    print(dataframe.head(head))
    print("############### NA  ###############")
    print(dataframe.isnull().sum())
    print("############### Quantiles  ###############")
    print(dataframe.describe([0, 0.85, 0.50, 0.95, 0.99, 1]).T)

check_df(ab_testing_kontrol)
check_df(ab_testing_test)

# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.
df_result = pd.concat([ab_testing_kontrol, ab_testing_test])

#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################
#  İstenilen test :  Average bidding'in maximum bidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B  testi yapmak istiyor

# Adım 1: Hipotezi tanımlayınız.
# H0 : M1 = M2  (average bidding'in maximum bidding'den daha fazla dönüşüm getirmez)
# H1 : M1!= M2

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz
ab_testing_kontrol["Purchase"].mean()
ab_testing_test["Purchase"].mean()

#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi  - AB Testing (Bağımsız İki Örneklem T Testi)
#####################################################
# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir. Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz

############################
# Normallik Varsayımı
############################
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.
# p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ

# Test sonucuna göre normallik varsayımı kontrol ve test grupları için sağlanıyor mu ? Elde edilen p-value değerlerini yorumlayınız.
test_stat, pvalue = shapiro(ab_testing_kontrol["Purchase"])
print(' ab_testing_kontrol : Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(ab_testing_test["Purchase"])
print('ab_testing_test : Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
############################
# Varyans Homojenliği :
############################
# H0: Varyanslar homojendir.
# H1: Varyanslar homojen Değildir.
# p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ
test_stat, pvalue = levene(ab_testing_kontrol["Purchase"], ab_testing_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

test_stat, pvalue = ttest_ind(ab_testing_kontrol["Purchase"], ab_testing_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#  Normal dağılım olmasaydı kullanılacak yöntem
# test_stat, pvalue = mannwhitneyu(ab_testing_kontrol["Purchase"], ab_testing_test["Purchase"])

# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

# p-değeri kontrolü
if pvalue > 0.05:
    print("p-değeri 0.05'ten büyük olduğu için H0 hipotezi reddedilemez.")
else:
    print("p-değeri 0.05'ten küçük olduğu için H0 hipotezi reddedilir. İki grup arasında istatistiksel olarak anlamlı bir fark vardır.")


##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.
# ttest_ind, iki bağımsız örneklem t-testini gerçekleştirmek için kullanılan bir işlevdir. İki grup arasındaki ortalamaların istatistiksel olarak farklı olup olmadığını belirlemek için kullanılır. Bu test, grupların normal dağılıma sahip olduğu ve varyanslarının homojen olduğu durumlarda kullanılabilir.


# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

