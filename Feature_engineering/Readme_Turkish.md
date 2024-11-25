# Özellik Mühendisliği

### **Veri Biliminde Özellik Mühendisliği (Feature Engineering) Nedir?**

Veri biliminde **Özellik Mühendisliği (Feature Engineering)**, ham veriden anlamlı ve model performansını artırabilecek nitelikler (özellikler) oluşturma sürecidir. Bu süreç, veri biliminde en kritik adımlardan biridir çünkü iyi tasarlanmış özellikler, bir modelin başarısını doğrudan etkiler. **Veri Temizliği** ile birleştirildiğinde, ham verinin analiz ve modelleme için optimize edilmesini sağlar.

## Konu Başlıkları ve Detayları

### **Outliers**  
Veri setindeki aykırı gözlemler ile mücadele etme yöntemleri hakkında beceriler ve bilgiler edindim. 

- Aykırı Değerler  
- Aykırı Değerleri Yakalama  
- Fonksiyonlaştırma  
- Aykırı Değerlere Erişmek  
- Aykırı Değer Problemini Çözme  
- Çok Değişkenli Aykırı Değer Analizi  

---

### **Missing Values**  
Veri setindeki eksik gözlemler ile mücadele etme yöntemleri hakkında beceriler ve bilgiler edindim.  

- Eksik Değerler  
- Eksik Değerleri Yakalama  
- Eksik Değer Problemini Çözme  
- Kategorik Değişken Kırılımında Değer Atama  
- Tahmine Dayalı Atama İşlemi  
- Eksik Verinin Yapısını İncelemek  
- Eksik Değerlerin Bağımlı Değişken ile Analizi  

---

### **Encoding Scaling**  
Veriyi makine öğrenmesine girmeden önce sayısal ifadelerle temsil etmemizi sağlayan LabelEncoder ve One-Hot Encoding yaklaşımları ve uzaklık temelli makine öğrenmesi algoritmalarında model performansını önemli ölçüde etkileyen değişken standartlaştırma ve dönüşüm işlemleri hakkında beceriler ve bilgiler edindim.  

- Label Encoding  
- One Hot Encoding  
- Rare Encoding  
- Rare Encoding Fonksiyonu  
- Özellik Ölçeklendirme  

---

### **Feature Extraction**  
Regular expression yardımıyla, ham veriyi temizleyerek anlamlı hale getirmek için kullanılan yöntemler hakkında beceriler ve bilgiler edindim.  

- Özellik Çıkarımı  
- Binary Features  
- Text Features  
- Regex Features  
- Date Features  
- Özellik Etkileşimleri  
---

### **Veri Temizliği ve Özellik Mühendisliği Sürecinde Yapılanlar ve Öğrenilenler**

#### **1. Ham Veriyi Temizleme**
- **Yapılanlar:**
  - Eksik, hatalı ya da uyumsuz veriler tespit edildi.
  - Eksik veriler çeşitli yöntemlerle dolduruldu (ortalama, medyan veya mode gibi).
  - Gerektiğinde eksik veya anlamsız gözlemler veri setinden çıkarıldı.  

- **Öğrenilenler:**
  - Veriyi analiz etmek ve eksiklikleri tespit etmek için kullanılan yaklaşımlar.
  - Eksik veya hatalı verileri düzeltmek için uygun stratejiler.

---

#### **2. Yeni Özellikler Çıkarma**
- **Yapılanlar:**
  - Verinin anlamını artırmak için yeni özellikler oluşturuldu (örneğin, tarih bilgisinden yıl, ay, gün çıkarıldı).
  - Mevcut değişkenler arasında matematiksel işlemlerle (toplama, çıkarma, oranlama) yeni özellikler oluşturuldu.
  - Metin verisinden kelime uzunluğu, kelime sayısı gibi özellikler elde edildi.  

- **Öğrenilenler:**
  - Veriyi zenginleştirmek için farklı yöntemlerle yeni özellikler çıkarma becerisi.
  - Çıkarılan özelliklerin model performansını nasıl etkilediğini analiz etme.

---

#### **3. Değişkenleri Dönüştürme**
- **Yapılanlar:**
  - Modele uygun olmayan değişkenler farklı formatlara dönüştürüldü (örneğin, kategorik değişkenler için bir-hot kodlama veya etiket kodlama yapıldı).
  - Sayısal değişkenler logaritma, karekök gibi yöntemlerle dönüştürüldü.
  - Değişkenlerin dağılımları normalleştirildi veya standartlaştırıldı.  

- **Öğrenilenler:**
  - Modele girmeye uygun olmayan değişkenleri dönüştürmek için kullanılan teknikler.
  - Özellik dönüşümünün model üzerindeki etkilerini değerlendirme becerisi.

---

#### **4. Özellik Seçimi**
- **Yapılanlar:**
  - Model performansına en çok katkı sağlayan özellikler seçildi.
  - Anlamsız ya da model için önemsiz değişkenler çıkarıldı.
  - Çoklu doğrusal bağımlılık (multicollinearity) gibi sorunlar tespit edilip çözüldü.  

- **Öğrenilenler:**
  - Model için en önemli özellikleri seçmek için kullanılan yöntemler (örneğin, korelasyon analizi, önem skoru).
  - Modelin aşırı karmaşıklığını önlemek için gereksiz değişkenlerin nasıl çıkarılacağı.

---

### **Genel Kazanımlar**
Bu süreçler sonucunda:  
- Ham veri analiz edilip temizlendi.
- Veri setinden anlamlı ve model performansını artıran özellikler çıkarıldı.
- Değişkenler modele uygun hale getirildi.
- Modelin doğruluğunu ve genelleme kapasitesini artıracak nitelikte bir veri seti oluşturuldu.

Bu öğrenilenler, herhangi bir makine öğrenimi projesinde güçlü bir temel oluşturmak için kullanılabilir.

---

### **Proje 1 : Diabete Feature Engineering (Diyabet Özellik Mühendisliği) **

---

### **Projenin Amacı:**  
Bu proje, ABD'deki Arizona eyaletinde yaşayan Pima Indian kadınları üzerinde yapılan bir çalışmadan elde edilen verilere dayanarak, kişilerin diyabet hastası olup olmadığını tahmin edebilecek bir makine öğrenmesi modeli geliştirmeyi amaçlamaktadır.  

### **İş Problemi:**  
Sağlık verilerinden faydalanarak diyabet hastalığını erken tespit etmek, doğru tedavi yöntemlerinin belirlenmesine ve bireylerin yaşam kalitesinin artırılmasına katkı sağlayabilir. Bu doğrultuda, özellik mühendisliği ve veri analizi süreçlerini kullanarak hedef değişken olan diyabet hastalığını tahmin edebilecek bir model oluşturulacaktır.  

### **Veri Seti Hikayesi:**  
Kullanılan veri seti, ABD'deki Ulusal Diyabet-Sindirim-Böbrek Hastalıkları Enstitüsü tarafından tutulan geniş bir veri havuzunun bir parçasıdır. Veri seti, Phoenix şehrinde yaşayan 21 yaş üzeri Pima Indian kadınlarının diyabet araştırması için toplanmıştır. Veri seti 768 gözlem biriminden ve 8 bağımsız değişkenden oluşmaktadır.  

### **Veri Seti Özellikleri:**  

| **Değişken Adı**            | **Açıklama**                                                    |
|-----------------------------|----------------------------------------------------------------|
| **Pregnancies**             | Kadının hamilelik sayısı                                       |
| **Glucose**                 | Kandaki glikoz seviyeleri                                      |
| **BloodPressure**           | Diastolik (küçük tansiyon) kan basıncı                        |
| **SkinThickness**           | Cilt kalınlığı (mm)                                           |
| **Insulin**                 | İnsülin seviyesi (mu U/ml)                                    |
| **BMI**                     | Vücut kitle indeksi (kg/m²)                                   |
| **DiabetesPedigreeFunction**| Soydaki diyabet hastalığı geçmişini ölçen bir fonksiyon        |
| **Age**                     | Bireyin yaşı                                                  |
| **Outcome**                 | Diyabet test sonucu (1 = pozitif, 0 = negatif)                |


### **Analiz ve Modelleme Süreci:**  

#### **1. Keşifçi Veri Analizi (EDA):**  
- **Genel İnceleme:** Veri setindeki değişkenlerin tanımlanması, özet istatistiklerin çıkarılması.  
- **Numerik ve Kategorik Değişkenlerin Analizi:** Her bir değişkenin özellikleri ve dağılımları incelendi.  
- **Hedef Değişken Analizi:** Hedef değişkenin (Outcome) bağımsız değişkenlerle ilişkisi analiz edildi.  
- **Eksik ve Aykırı Değer Analizi:** Glukoz, insülin gibi değişkenlerdeki sıfır değerler eksik değer olarak ele alındı ve aykırı gözlemler kontrol edildi.  

#### **2. Özellik Mühendisliği (Feature Engineering):**  
- Eksik değerlerin doldurulması ve aykırı gözlemlerin eşik değerlerle baskılanması.  
- Yeni özellikler oluşturma:  
  - **Yaş Kategorileri (NEW_AGE_CAT):** "Mature" ve "Senior" grupları.  
  - **BMI Kategorileri (NEW_BMI):** "Underweight", "Healthy", "Overweight", "Obese".  
  - **Glukoz Seviyesi Kategorileri (NEW_GLUCOSE):** "Normal", "Prediabetes", "Diabetes".  
  - Yaş ve BMI kombinasyonlarına dayalı kategoriler.  
  - İnsülin değerlerine dayalı kategoriler.  

#### **3. Encoding İşlemleri:**  
Kategorik değişkenler etiketleme ve one-hot encoding yöntemleriyle modele hazır hale getirildi.  

#### **4. Modelleme:**  
Random Forest gibi güçlü algoritmalar kullanılarak tahmin modeli geliştirildi ve başarı metrikleri (accuracy, precision, recall, F1-score, ROC-AUC) hesaplandı.  

### **Çıktılar ve Faydalar:**  
- Diyabet hastalığının erken teşhisini sağlayacak bir model.  
- Sağlık alanında bireyselleştirilmiş tedaviye yönelik kararların desteklenmesi.  
- Yeni özellikler sayesinde veri setinden daha anlamlı içgörüler elde edilmesi.  


## Proje Dosyaları  

- **Veri Seti :** [diabetes.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/datasets/diabetes.csv)  
- **Kod Dosyası:** [Diabete Feature Engineering (Diyabet Özellik Mühendisliği)](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/diabetes_feature_engineering.py)  

---
### **Proje 2 : Telco Customer Churn Feature Engineering **

---
### **Proje Amacı:**  
Bir telekomünikasyon şirketinin müşteri davranışlarını anlamak ve hangi müşterilerin hizmetten ayrılma (churn) eğiliminde olduğunu tahmin edebilecek bir makine öğrenmesi modeli geliştirmek.  

### **Veri Seti Hikayesi:**  
Bu veri seti, Kaliforniya'da faaliyet gösteren hayali bir telekomünikasyon şirketinin üçüncü çeyrekteki müşteri bilgilerini içerir. 7043 müşteri gözlemi ve 21 değişkenden oluşan bu veri seti, müşterilerin demografik özelliklerini, aldıkları hizmetleri, hesap bilgilerini ve ayrılıp ayrılmadıklarını içermektedir. Amaç, müşterilerin churn eğilimini analiz ederek müşteri kaybını önleyici aksiyonlar alabilmektir.  

### **Değişkenler:**  

| **Değişken Adı**     | **Açıklama**                                                                 | **Tip**                |
|-----------------------|-----------------------------------------------------------------------------|------------------------|
| **CustomerId**        | Müşteri ID’si                                                             | Kategorik              |
| **Gender**            | Cinsiyet                                                                  | Kategorik              |
| **SeniorCitizen**     | Müşterinin yaşlı olup olmadığı (1: Evet, 0: Hayır)                         | Kategorik              |
| **Partner**           | Müşterinin bir ortağı olup olmadığı (Evet, Hayır)                         | Kategorik              |
| **Dependents**        | Müşterinin bakmakla yükümlü olduğu kişiler olup olmadığı (Evet, Hayır)     | Kategorik              |
| **tenure**            | Müşterinin şirkette kaldığı ay sayısı                                      | Sayısal (Sürekli)      |
| **PhoneService**      | Müşterinin telefon hizmeti olup olmadığı (Evet, Hayır)                    | Kategorik              |
| **MultipleLines**     | Müşterinin birden fazla hattı olup olmadığı                                | Kategorik              |
| **InternetService**   | Müşterinin internet servis sağlayıcısı (DSL, Fiber optik, Hayır)          | Kategorik              |
| **OnlineSecurity**    | Müşterinin çevrimiçi güvenliği (Evet, Hayır, İnternet hizmeti yok)         | Kategorik              |
| **OnlineBackup**      | Müşterinin online yedeği (Evet, Hayır, İnternet hizmeti yok)              | Kategorik              |
| **DeviceProtection**  | Müşterinin cihaz koruması (Evet, Hayır, İnternet hizmeti yok)             | Kategorik              |
| **TechSupport**       | Müşterinin teknik destek alıp almadığı (Evet, Hayır, İnternet hizmeti yok)| Kategorik              |
| **StreamingTV**       | Müşterinin TV yayını olup olmadığı                                         | Kategorik              |
| **StreamingMovies**   | Müşterinin film akışı olup olmadığı                                       | Kategorik              |
| **Contract**          | Müşterinin sözleşme süresi (Aydan aya, Bir yıl, İki yıl)                  | Kategorik              |
| **PaperlessBilling**  | Müşterinin kağıtsız faturası olup olmadığı (Evet, Hayır)                  | Kategorik              |
| **PaymentMethod**     | Müşterinin ödeme yöntemi                                                  | Kategorik              |
| **MonthlyCharges**    | Müşteriden aylık olarak tahsil edilen tutar                               | Sayısal (Sürekli)      |
| **TotalCharges**      | Müşteriden tahsil edilen toplam tutar                                     | Sayısal (Sürekli)      |
| **Churn**             | Müşterinin ayrılıp ayrılmadığı (Evet, Hayır)                              | Kategorik (Hedef)      |  

### **Veri Kategorileri:**  
1. **Hizmet Verileri:**  
   - Telefon, internet, güvenlik, yedekleme, cihaz koruma, teknik destek, TV yayını, film akışı.  
2. **Hesap Bilgileri:**  
   - Müşteri kalma süresi, sözleşme tipi, ödeme yöntemi, kağıtsız faturalandırma, aylık ve toplam ücretler.  
3. **Demografik Veriler:**  
   - Cinsiyet, yaş aralığı, partner durumu, bakmakla yükümlü olunan kişi bilgisi.


Bu çalışmada, **Telco-Customer-Churn** veri seti üzerinde müşteri kaybı (churn) ile ilişkili faktörlerin analizi ve tahmin modelleri geliştirilmesi hedeflenmiştir. Kullanılan teknolojiler ve yapılan işlemler şu şekilde açıklanabilir:

---

## **1. Kullanılan Teknolojiler**
- **Python**: Veri analizi ve modelleme için.
- **Kütüphaneler**:
  - **Pandas**: Veri manipülasyonu ve temizliği.
  - **NumPy**: Sayısal hesaplamalar.
  - **Matplotlib & Seaborn**: Veri görselleştirme.
  - **Scikit-learn**: Makine öğrenimi modelleri ve metrikleri.
  - **CatBoost, LightGBM, XGBoost**: Güçlü sınıflandırma algoritmaları.

---

## **2. Çalışmanın Adımları**

### **A. Veri Yükleme ve Ön İşleme**
1. **Veri Yükleme**: Telco-Customer-Churn veri seti yüklendi.
2. **Veri Tiplerinin Düzeltilmesi**: 
   - `TotalCharges` sütunu sayısal bir değişken olarak dönüştürüldü.
   - `Churn` sütunu, ikili sınıflandırma (1: Evet, 0: Hayır) olarak yeniden kodlandı.

### **B. Keşifçi Veri Analizi (EDA)**

#### 1. **Genel Resim**
- **Şekil, veri tipleri, eksik değerler** ve **istatistiksel özet** elde edildi.

#### 2. **Değişkenlerin Türlerine Göre Ayrılması**
- Kategorik, sayısal ve kardinal değişkenler belirlendi.
- **Kategorik değişkenlerin analizi**:
  - Örneğin, müşterilerin çoğu (yaklaşık %60) "kağıtsız fatura" seçeneğini kullanmakta.
  - Fiber optik internet kullanıcılarının churn oranı yüksek.
- **Sayısal değişkenlerin analizi**:
  - Örneğin, yeni müşteriler (tenure = 1) churn etme eğiliminde.
  - Daha yüksek aylık ücretler, churn olasılığını artırıyor.

#### 3. **Hedef Değişken Analizi (Churn ile İlişkiler)**
- Kategorik değişkenlerin churn ile ilişkisi analiz edildi:
  - **Kısa dönemli (aylık) sözleşmeler**, churn oranının artmasına neden oluyor.
  - **ElectronicCheck ödeme yöntemini kullanan müşterilerin** churn oranı daha yüksek.
- Sayısal değişkenlerin churn ile ilişkisi analiz edildi:
  - **Tenure** uzunluğu arttıkça churn oranı azalıyor.
  - **MonthlyCharges** değeri arttıkça churn oranı artıyor.

#### 4. **Korelasyon Analizi**
- Korelasyon matrisi:
  - **TotalCharges** ve **MonthlyCharges** arasında yüksek korelasyon görüldü.
  - **Churn** ile **tenure** arasında ters yönlü bir ilişki mevcut.

---
## **Feature Engineering (Özellik Mühendisliği)**
---
### 1. **Eksik Değer Analizi ve İşlemleri**
- **Eksik değer tespiti:** `missing_values_table` fonksiyonu, eksik değerleri ve yüzdelerini etkin bir şekilde tespit ediyor.
- **Eksik değer doldurma:** `TotalCharges` için eksik değerler `MonthlyCharges` kullanılarak doldurulmuş. Bu yöntem mantıklı ancak eksik değerlerin başka değişkenlerle tahmin edilmesini içeren bir model de denenebilir (örneğin, regresyonla doldurma).

---

### 2. **Aykırı Değer Analizi ve Baskılama**
- **Eşik değerlerin hesaplanması:** `outlier_thresholds` ve `check_outlier` fonksiyonları, esnek aykırı değer analizi sunuyor.
- **Baskılama:** `replace_with_thresholds` ile aykırı değerler baskılanmış. Alternatif olarak, aykırı değerlerin etkisini azaltmak için logaritmik dönüşümler veya robust scaler gibi teknikler düşünülebilir.

---

### 3. **Özellik Çıkarımı**
- **Yaratıcı yeni değişkenler:** `NEW_TENURE_YEAR`, `NEW_Engaged`, `NEW_noProt`, `NEW_TotalServices` gibi değişkenler, müşteri davranışlarını anlamada önemli katkılar sağlayabilir. 
- **Matematiksel özellikler:** `NEW_AVG_Charges` ve `NEW_Increase` gibi değişkenler, hizmetlerin müşteri üzerindeki mali etkilerini ölçmek için faydalı.

**Öneri:** 
Bazı özelliklerin doğrusal ilişkilerini kontrol etmek için korelasyon analizi yapılabilir. Yüksek korelasyon varsa, değişken seçimi tekrar gözden geçirilebilir.

---

### 4. **Kod Yapısının Genel Değerlendirmesi**
- **Kategori ve Sayısal Değişkenlerin Ayrımı:** `grab_col_names` fonksiyonunun kullanımı, kodun düzenli olmasını sağlıyor.
- **Kodların Modülerliği:** Etkileşimli fonksiyonlar (örneğin, `one_hot_encoder`, `label_encoder`) analiz sürecini esnek hale getirmiş.

---

### 5. **Model Performansları**
Çeşitli modellerin performansları değerlendirilmiş ve sonuçlar aşağıdaki gibi görünüyor:

| Model       | Accuracy | AUC  | Recall | Precision | F1    |
|-------------|----------|------|--------|-----------|-------|
| **LR**      | 0.7999   | 0.840| 0.5003 | 0.6645    | 0.5699|
| **KNN**     | 0.7701   | 0.753| 0.4666 | 0.5851    | 0.5182|
| **CART**    | 0.7302   | 0.660| 0.5067 | 0.4922    | 0.4992|
| **RF**      | 0.7934   | 0.827| 0.5072 | 0.6404    | 0.5659|
| **XGB**     | 0.7907   | 0.826| 0.5153 | 0.6296    | 0.5664|
| **LightGBM**| 0.7940   | 0.836| 0.5222 | 0.6374    | 0.5738|
| **CatBoost**| 0.7970   | 0.840| 0.5051 | 0.6531    | 0.5691|

- **Güçlü performans:** Logistic Regression ve CatBoost modelleri özellikle AUC ve accuracy açısından güçlü görünüyor.
- **Recall geliştirme fırsatı:** Recall oranları diğer metriklere göre düşük. Bu, pozitif sınıfın (örneğin churn eden müşteriler) daha iyi tespit edilmesi için optimize edilebilir.

**Öneriler:**
- **Hiperparametre optimizasyonu:** GridSearchCV veya RandomizedSearchCV ile modellerin hiperparametrelerini optimize ederek performans artırılabilir.
- **Özellik seçimi:** Recursive Feature Elimination (RFE) gibi yöntemlerle özellikler azaltılarak modeller sadeleştirilebilir.
---

Elde edilen bulgular, müşteri kaybını önlemek için firmalara rehberlik edebilir. Örneğin:
- **Sözleşme sürelerini uzatmaya yönelik kampanyalar**, churn oranını düşürebilir.
- **ElectronicCheck yerine diğer ödeme yöntemlerinin teşvik edilmesi** churn'ü azaltabilir.


## Proje Dosyaları  

- **Veri Seti :** [Telco-Customer-Churn.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/datasets/Telco-Customer-Churn.csv)  
- **Kod Dosyası:** [Telco_Churn.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/Telco_Churn.py)  

---
**Berna Uzunoğlu | Python Developer | Data Scientist**