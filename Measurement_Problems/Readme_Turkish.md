
# Ölçümleme Problemleri

Ürünlerin puanlanmasında kullanılan yaklaşımlar ve satın alma kararlarımızı etkileyen en önemli faktör olan yorum ve rating'lerin sıralanma yöntemleri ile ilgili beceriler edindim.   

## Konu Başlıkları ve Detayları  

### 1.Rating Products (Ürün Puanlama) 
Ürünlerin puanlanmasında kullanılan yaklaşımlar üzerine detaylı bilgi edindim. İstatistiksel yöntemler kullanılarak en yansız puanlama yöntemlerinin nasıl oluşturulabileceğini öğrendim. İncelenen yaklaşımlar arasında:  
- Ortalama Puan Hesaplama  
- Puan Zamanlarına Göre Ağırlıklı Ortalama  
- Kullanıcı Temelli Ağırlıklı Ortalama  
- Ağırlıklı Derecelendirme  

### 2.Sorting Products (Ürün Sıralama)  
Ürünlerin aldığı yorum ve puanların, satın alma kararlarımız üzerindeki etkilerini inceledim. Kullanıcılar tarafından yapılan yorum ve verilen ratinglerin sıralanmasında kullanılan yöntemleri öğrendim. Ele alınan yöntemler:  
- Derecelendirmeye Göre Sıralama  
- Yorum ve Satın Alma Sayısına Göre Sıralama  
- Derecelendirme, Satın Alma ve Yoruma Göre Sıralama  
- Bayes Ortalama Derecelendirme Puanı  
- Karma Sıralama  
- IMDB Film Puanlama ve Sıralama Yöntemleri  

### 3.Sorting Reviews (Yorum Sıralama)  
Kullanıcıların satın alma kararlarında önemli bir etkisi olan yorumların sıralanma yöntemlerini öğrendim. Bu yöntemler:  
- Üst-Alt Farkı Skoru  
- Ortalama Puan Hesaplama  
- Wilson Alt Sınır Puanı  

### 4.AB Testing (AB Testi)  
İki grup arasındaki farkları anlamaya yönelik A/B testi yöntemleri ve istatistiksel analizler üzerinde çalıştım. Öğrendiğim konular şunlardır:  
- Örneklem ve Betimsel İstatistikler  
- Güven Aralıkları ve Hipotez Testleri  
- Bağımsız İki Örneklem T Testi  
- İki Grup Oranı Karşılaştırma Testi  
- İkiden Fazla Grup Ortalaması Karşılaştırma (ANOVA)  

# Proje 1 : AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması (Facebook)

Bu projede, Facebook reklam teklif stratejilerinden **Maximum Bidding** ve **Average Bidding** yöntemlerinin satın alma performanslarını (**Purchase**) karşılaştırmak amacıyla bir **A/B testi** gerçekleştirilmiştir.

## İş Problemi  
Facebook, mevcut **Maximum Bidding** teklif verme türüne alternatif olarak yeni bir teklif türü olan **Average Bidding**'i tanıttı.  
Müşterimiz **bombabomba.com**, bu yeni özelliği test etmeye karar verdi. Amaç, Average Bidding'in Maximum Bidding'den daha fazla dönüşüm getirip getirmediğini anlamaktır. Test sonuçlarına göre, reklam stratejilerinin etkinliği değerlendirilecektir.  

---

## Veri Seti Hikayesi  

Veri seti, kontrol ve test gruplarını içermektedir. Her grupta reklamların görüntülenme ve tıklanma sayılarından elde edilen satın alma ve gelir bilgileri bulunmaktadır.  

- **Kontrol Grubu:** Maximum Bidding yöntemi uygulanmıştır.  
- **Test Grubu:** Average Bidding yöntemi uygulanmıştır.  

 ### Değişkenler:
Her iki grup için aşağıdaki değişkenler yer almaktadır:  

| Değişken     | Açıklama                                          |
|--------------|---------------------------------------------------|
| **Impression**| Reklam görüntüleme sayısı                        |
| **Click**     | Reklamlara yapılan tıklama sayısı                 |
| **Purchase**  | Tıklanan reklamlardan sonra yapılan satın alma sayısı |
| **Earning**   | Satın alımlardan elde edilen gelir                |
 

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

# Proje 2 :Rating Product & Sorting Reviews in Amazon

## Proje Amacı
E-ticaretteki temel problemlerden biri, ürünlere verilen puanların ve yorumların doğru şekilde hesaplanmasıdır. Bu proje, bir ürünün ortalama puanını güncel yorumlara göre ağırlıklandırarak hesaplamayı ve ürün detay sayfasında görünen yorumları sıralamayı hedeflemektedir. Böylece daha doğru ürün puanları ve güvenilir yorumlar elde edilecek, kullanıcılar ve satıcılar için daha verimli bir alışveriş deneyimi sağlanacaktır.

## İş Problemi
 E-ticaretteki en önemli problemlerden bir tanesi ürünlere satış sonrası verilen puanların doğru şekilde hesaplanmasıdır. Bu problemin çözümü e-ticaret sitesi için daha fazla müşteri memnuniyeti sağlamak, satıcılar için ürünün öne çıkması ve satın alanlar için sorunsuz bir alışveriş deneyimi demektir. Bir diğer problem ise ürünlere verilen yorumların doğru bir şekilde sıralanması olarak karşımıza çıkmaktadır. Yanıltıcı yorumların öne çıkması ürünün satışını doğrudan etkileyeceğinden dolayı hem maddi kayıp hem de müşteri kaybına neden olacaktır. Bu 2 temel problemin çözümünde e-ticaret sitesi ve satıcılar satışlarını arttırırken müşteriler ise satın alma yolculuğunu sorunsuz olarak tamamlayacaktır.

## Veri Seti Hikayesi
Amazon ürün verilerini içeren bu veri seti, elektronik kategorisindeki ürünler üzerine yapılan yorumları ve kullanıcı puanlarını içermektedir. Her bir yorum, ürün hakkında verilen puan (overall), yorum metni (reviewText), yorumun faydalı bulunma sayısı (helpful_yes), ve toplam oy sayısı (total_vote) gibi metadatalarla birlikte sunulmaktadır.

### Değişkenler:
| Değişken       | Açıklama                                                                 |
|----------------|--------------------------------------------------------------------------|
| **reviewerID** | Kullanıcı ID’si                                                           |
| **asin**       | Ürün ID’si                                                                |
| **reviewerName**| Kullanıcı Adı                                                            |
| **helpful**    | Faydalı değerlendirme derecesi                                            |
| **reviewText** | Değerlendirme                                                             |
| **overall**    | Ürün rating’i                                                             |
| **summary**    | Değerlendirme özeti                                                      |
| **unixReviewTime**| Değerlendirme zamanı - Unix zaman damgası, 1 Ocak 1970'ten bu yana geçen saniye sayısını temsil eder. |
| **reviewTime** | Değerlendirme zamanı (Raw)                                                |
| **day_diff**   | Değerlendirmeden itibaren geçen gün sayısı                                |
| **helpful_yes**| Değerlendirmenin faydalı bulunma sayısı                                   |
| **total_vote** | Değerlendirmeye verilen oy sayısı                                         |

## Proje Süreci

1. **Veri Setinin İncelenmesi**:
   - Veri seti okundu ve ürünlere ait temel bilgiler incelendi.
   - Veri setinde eksik değerler kontrol edildi.

2. **Görev 1: Ortalama Puanın Hesaplanması ve Karşılaştırılması**:
   - Ürünlerin ortalama puanları, mevcut "overall" sütunundan elde edilerek hesaplandı.
   - Ayrıca, yorumların tarihine dayalı ağırlıklı ortalamalar hesaplanarak, ürünlerin daha güncel değerlendirmeleri ön plana çıkarıldı.

3. **Görev 2: En Faydalı Yorumların Seçilmesi**:
   - "helpful_no" değişkeni oluşturularak, kullanıcıların olumlu ya da olumsuz bulduğu yorumlar arasındaki fark hesaplandı.
   - "score_pos_neg_diff", "score_average_rating" ve "wilson_lower_bound" gibi metrikler kullanılarak her bir yoruma güvenilirlik puanları verildi.

4. **Sonuçların Değerlendirilmesi**:
   - Wilson alt sınırına göre sıralanan en faydalı 20 yorum belirlendi ve sıralama yapılarak ürünlerin en güvenilir yorumları ön plana çıkarıldı.

## Teknik Yöntemler ve Uygulamalar
- **Puan Ağırlıklandırma**: Yorumlar, zaman dilimlerine göre ağırlıklandırıldı ve daha eski yorumlar, daha yeni olanlara göre daha düşük puan aldı.
- **Veri Temizleme ve Hazırlama**: Eksik veriler kontrol edilerek temizlendi ve gerekli dönüşümler yapıldı.
- **Yorum Sıralaması**: "helpful_no", "score_pos_neg_diff", "score_average_rating" ve "wilson_lower_bound" gibi metrikler kullanılarak güvenilir yorumlar sıralandı.

## Sonuçlar
- Güncel yorumların ağırlıklı puan hesaplamasında etkili olduğu gözlemlendi.
- "Wilson Lower Bound" metodu, yanıltıcı yorumları filtreleyerek, en güvenilir yorumları ön plana çıkarmada başarılı oldu.
- Bu projeyle, kullanıcılar ve satıcılar için daha doğru ve güvenilir ürün yorumları sunulmuş oldu, böylece alışveriş deneyimi daha verimli hale getirildi.

## Proje Dosyaları  

- **Veri Seti:** [amazon_review.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/datasets/amazon_review.csv)  
- **Kod Dosyası:** [Rating Product & Sorting Reviews in Amazon.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/Rating%20Product%20%26%20Sorting%20Reviews%20in%20Amazon.py)  

---
**Berna Uzunoğlu | Python Developer | Data Scientist**
