# AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması (Facebook)

Bu projede, Facebook reklam teklif stratejilerinden **Maximum Bidding** ve **Average Bidding** yöntemlerinin satın alma performanslarını (**Purchase**) karşılaştırmak amacıyla bir **A/B testi** gerçekleştirilmiştir.

## İş Problemi  
Facebook, mevcut **Maximum Bidding** teklif verme türüne alternatif olarak yeni bir teklif türü olan **Average Bidding**'i tanıttı.  
Müşterimiz **bombabomba.com**, bu yeni özelliği test etmeye karar verdi. Amaç, Average Bidding'in Maximum Bidding'den daha fazla dönüşüm getirip getirmediğini anlamaktır. Test sonuçlarına göre, reklam stratejilerinin etkinliği değerlendirilecektir.  

---

## Veri Seti Hikayesi  

Veri seti, kontrol ve test gruplarını içermektedir. Her grupta reklamların görüntülenme ve tıklanma sayılarından elde edilen satın alma ve gelir bilgileri bulunmaktadır.  

- **Kontrol Grubu:** Maximum Bidding yöntemi uygulanmıştır.  
- **Test Grubu:** Average Bidding yöntemi uygulanmıştır.  

Her iki grup için aşağıdaki değişkenler yer almaktadır:  

- **Impression:** Reklam görüntüleme sayısı.  
- **Click:** Reklamlara yapılan tıklama sayısı.  
- **Purchase:** Tıklanan reklamlardan sonra yapılan satın alma sayısı.  
- **Earning:** Satın alımlardan elde edilen gelir.  

---

## A/B Testi Süreci  

### 1. Hipotezlerin Kurulması  
- **H0 Hipotezi:** Average Bidding yöntemi, Maximum Bidding yöntemine göre daha fazla dönüşüm sağlamaz.  
  \(H_0: \mu_{control} = \mu_{test}\)  
- **H1 Hipotezi:** Average Bidding yöntemi, Maximum Bidding yöntemine göre daha fazla dönüşüm sağlar.  
  \(H_1: \mu_{control} \neq \mu_{test}\)  

---

### 2. Varsayım Kontrolleri  
A/B testinin doğruluğu için iki temel varsayım test edilmiştir:  

#### a. Normallik Varsayımı  
- **Shapiro-Wilk Testi** ile grupların normallik varsayımı test edilmiştir.  
  - **Kontrol Grubu:** \(p = 0.5891\) → Normallik varsayımı sağlanıyor.  
  - **Test Grubu:** \(p = 0.1541\) → Normallik varsayımı sağlanıyor.  

#### b. Varyans Homojenliği Varsayımı  
- **Levene Testi** ile grupların varyanslarının eşit olup olmadığı test edilmiştir.  
  - **Sonuç:** \(p = 0.1083\) → Varyans homojenliği sağlanıyor.  

---

### 3. Hipotez Testi  
- Varsayım testlerinden sonra **Bağımsız İki Örneklem T Testi (ttest_ind)** uygulanmıştır.  
- **Sonuç:**  
  - \(p = 0.3493\): H0 reddedilemez.  
  - İki grup arasında satın alma ortalamaları açısından istatistiksel olarak anlamlı bir fark bulunmamıştır.  

---

## Sonuçların Analizi ve Öneriler  

### 1. Sonuçların Yorumu  
- A/B testi sonuçlarına göre, **Average Bidding** ve **Maximum Bidding** yöntemleri arasında satın alma (Purchase) açısından istatistiksel olarak anlamlı bir fark bulunmamıştır.  

### 2. Müşteriye Öneriler  
- Test edilen yeni teklif stratejisi şu an için önemli bir avantaj sağlamamaktadır.  
- Daha uzun bir süre boyunca veya daha büyük bir örneklemle yeni bir A/B testi yapılabilir.  
- Alternatif metrikler (örneğin, kullanıcı başına gelir, reklam tıklama oranı) üzerinde analizler yapılabilir.  
- Stratejide iyileştirme veya farklı kullanıcı segmentleri için özelleştirilmiş teklifler düşünülebilir.  

---

## Teknik Yöntem ve Uygulamalar  

Proje boyunca aşağıdaki yöntem ve araçlar kullanılmıştır:  

1. **Veri Hazırlama ve Keşifsel Veri Analizi (EDA)**  
   - Kontrol ve test grubu verileri birleştirilip incelenmiştir.  

2. **İstatistiksel Testler:**  
   - **Normallik Varsayımı:** Shapiro-Wilk Testi  
   - **Varyans Homojenliği:** Levene Testi  
   - **Hipotez Testi:** Bağımsız İki Örneklem T Testi  

---

## Proje Dosyaları  

- **Veri Seti:** [ab_testing.xlsx](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/datasets/ab_testing.xlsx)  
- **Kod Dosyası:** [AB_Testing_Study.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/AB_Testing_Study.py)  

---

**Berna Uzunoğlu | Python Developer | Data Scientist**
