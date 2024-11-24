# Tavsiye Sistemleri 

Tavsiye sistemleri (Recommendation Systems), kullanıcıların ilgisini çekebilecek ürün, hizmet veya içerikleri otomatik olarak öneren makine öğrenimi tabanlı sistemlerdir. E-ticaret, müzik platformları, video akış hizmetleri ve sosyal medya gibi birçok alanda kullanılan bu sistemler, kullanıcı deneyimini iyileştirirken, şirketlerin satış ve müşteri memnuniyetini artırmasına katkı sağlar.

### **Tavsiye Sistemlerinin Temel Çalışma Mantığı**

Tavsiye sistemleri, kullanıcıların geçmiş davranışlarını, tercihlerini ve diğer kullanıcılarla olan ilişkilerini analiz ederek öneriler oluşturur. Çalışma mantığını üç ana başlıkta ele alabiliriz:

---
## Konu Başlıkları ve Detayları

#### 1. **Birliktelik Kuralı Öğrenimi (Association Rule Learning)**

Birliktelik kuralı öğrenimi, özellikle perakende sektöründe kullanılan bir tekniktir. Amaç, müşterilerin alışverişlerinde bir arada satın aldıkları ürünler arasındaki ilişkiyi keşfetmektir. 

- **Örnek Uygulama**: Market sepet analizinde, "Eğer müşteri ekmek alırsa, genellikle süt de alır" gibi sonuçlar çıkarılır.
- **Avantajları**:
  - Hızlı uygulanabilir.
  - Basit veri yapılarıyla çalışır.
- **Dezavantajları**:
  - Sadece geçmiş verilere dayanır, yeni kullanıcı veya ürünlerle çalışmakta zorlanır.
  
   -  Apriori Algoritması
   -  Apriori Nasıl Çalışır?
   -  Birliktelik Kuralı Temelli Tavsiye Sistemi
   -  Birliktelik Kuralı Öğrenimi
   -  Veri Ön İşleme
   -  Arl Veri Yapılarını Hazırlamak
   -  Birliktelik Kuralları Analizi
   -  Çalışmanın Scriptini Hazırlama
   -  Ürün Önerme Uygulaması

---
#### 2. **İçerik Temelli Filtreleme (Content-Based Recommendation)**

Bu yöntemde, öneriler bir ürünün içerik özelliklerine dayalı olarak yapılır. Kullanıcıların beğendiği ürünlerin özellikleri analiz edilerek, bu özelliklere benzer ürünler önerilir.

- **Örnek Uygulama**: Netflix’te bir kullanıcı aksiyon filmi izlemeyi seviyorsa, içerik özellikleri benzer başka aksiyon filmleri önerilir.
- **Kullanılan Teknikler**:
  - **TF-IDF**: Metin bazlı verilerde sıkça kullanılan bir teknik. Anahtar kelimelerin önemini ölçerek benzerlik analizi yapılır.
  - **Cosine Similarity**: İçerik özellikleri arasındaki benzerliği ölçmek için kullanılır.
- **Avantajları**:
  - Kullanıcı geçmişine ihtiyaç duymaz.
  - Ürünler arasındaki içerik benzerliğini kullanır.
- **Dezavantajları**:
  - Kullanıcıyı yeni ürünlerle tanıştırmakta sınırlıdır (sadece benzer içerikleri önerir).
 
   - Count Vector
   - Metin Vektörleştirme
   - İçerik Temelli Tavsiye Sistemleri
   - TF-IDF Matrisinin Oluşturulması
   - Cosine Sim Hesaplama
   - Benzerliklerine Göre Önerilerin Yapılması
   - Çalışmanın Scriptini Hazırlama
---

#### 3. **İş Birlikçi Filtreleme (Collaborative Filtering)**

Kullanıcıların geçmiş davranışlarına ve diğer kullanıcılarla olan benzerliklerine dayanarak öneriler oluşturur. 

- **Yöntemleri**:
  - **User-Based Collaborative Filtering**: Benzer kullanıcıların tercihlerini analiz ederek öneriler sunar.
  - **Item-Based Collaborative Filtering**: Benzer ürünler arasındaki ilişkileri kullanarak öneriler yapar.
- **Örnek Uygulama**: Spotify'da benzer müzik zevkine sahip kullanıcıların oluşturduğu listelere dayanarak şarkı önerisi yapılması.
- **Avantajları**:
  - Kullanıcı davranışlarından öğrenir.
  - İçerik özelliklerine ihtiyaç duymaz.
- **Dezavantajları**:
  - **Cold-Start Problemi**: Yeni kullanıcı veya ürünlerle çalışmada zorluk.
  - Büyük veri kümelerinde hesaplama maliyeti yüksek olabilir.

  - Item-Based Tavsiye Sistemi
  - Item-Based İş Birlikçi Filtreleme
  - User Movie Df'in Oluşturulması
  - Item-Based Film Önerilerinin Yapılması
  - Çalışmanın Scriptini Hazırlama
  - Kullanıcı Tabanlı İş Birlikçi Filtreleme
  - Kullanıcı Tabanlı İş Birlikçi Filtreleme
  - Veri Setini Hazırlama
  - İzlenen Filmleri Getirme Uygulaması
  - Aynı Filmleri İzleyen Diğer Kullanıcılar
  - Benzerliklerin Belirlenmesi
  - Skor Hesaplama
  - Çalışmanın Fonksiyonlaştırılması

---

#### 4. **Model Tabanlı Yaklaşımlar (Model-Based Methods)**

Model tabanlı yöntemler, daha sofistike algoritmalar ve matematiksel modeller kullanır. Bu yöntemlerden biri **Matris Çarpanlarına Ayırma (Matrix Factorization)** tekniğidir. Kullanıcıların ve ürünlerin özellik vektörlerini çıkararak, öneriler bu vektörler arasındaki ilişkilere göre yapılır.

- **Örnek Uygulama**: Amazon'da bir kullanıcının daha önce puanlamadığı bir ürüne kaç puan vereceğinin tahmini.
- **Avantajları**:
  - Eksik veri setleriyle iyi çalışır.
  - Karmaşık ilişkileri modelleyebilir.
- **Dezavantajları**:
  - Daha fazla işlem gücü ve hesaplama süresi gerektirir.

  - Gradyan İniş
  - Verinin Hazırlanması
  - Modelleme
  - Model Kurma 
  - Final Model ve Tahmin
---

### **Tavsiye Sistemlerinin Kullanım Alanları**

- **E-ticaret**: Ürün önerileri (Amazon, eBay).
- **Müzik ve Video Platformları**: Şarkı ve film önerileri (Spotify, Netflix).
- **Sosyal Medya**: Takipçi önerileri, içerik önerileri (Instagram, Twitter).
- **Eğitim**: Online kurs önerileri (Coursera, Udemy).

- Tavsiye sistemleri, kullanıcıları daha iyi tanıyarak kişiselleştirilmiş deneyimler sunar. Bu da hem kullanıcı memnuniyetini artırır hem de işletmelerin gelirlerini yükseltir.

### **Proje: Armut Hizmet Platformunda Birliktelik Kurallarına Dayalı Hizmet Öneri Sistemi**  

---

### **Projenin Amacı**  
Türkiye'nin en büyük online hizmet platformlarından biri olan Armut için, müşterilerin aldıkları hizmetler arasındaki ilişkileri tespit ederek, **Association Rule Learning** yöntemleriyle içerik temelli bir ürün öneri sistemi geliştirmek.  

Bu sistem sayesinde, kullanıcıların satın aldığı hizmetlere benzer hizmetler önerilebilir ve kullanıcı deneyimi geliştirilebilir.

---

### **İş Problemi**  
Armut platformunda, kullanıcıların aldıkları hizmetlere yönelik bir sepet tanımı bulunmamaktadır. Kullanıcıların aylık olarak aldığı hizmetler birer sepet olarak tanımlanmış ve bu sepetler arasında birliktelik kuralları çıkarılmıştır. Amaç, geçmişte alınan hizmetlere dayanarak müşterilere en olası diğer hizmet önerilerini yapmaktır.  

---

### **Veri Setinin Hikayesi** 

Veri seti, kullanıcıların farklı kategoriler altındaki hizmetleri nasıl kullandığını ve bu hizmetlerin zamanla nasıl değiştiğini incelemek için uygundur.  

### Değişkenler

| **Değişken**   | **Açıklama**                                                                 |
|----------------|------------------------------------------------------------------------------|
| **UserId**     | Her bir müşteri için benzersiz bir tanımlayıcı.                              |
| **ServiceId**  | Her kategoriye ait anonimleştirilmiş hizmetlerin tanımlayıcısı.              |
| **CategoryId** | Hizmetlerin kategorisini ifade eden anonimleştirilmiş ID.                   |
| **CreateDate** | Hizmetin satın alındığı tarih.                                              |

---

### **Kullanılan Teknolojiler ve Yöntemler**  

#### **1. Veri Ön İşleme**  
- Veri seti pandas kullanılarak yüklendi ve incelendi.  
- **ServiceId** ve **CategoryId** birleştirilerek benzersiz bir **Hizmet** sütunu oluşturuldu.  
- Aylık sepet tanımı oluşturmak için kullanıcıların hizmet alma tarihleri yıllık-aylık formatta birleştirildi.  
- Kullanıcı ve tarih bilgisiyle birleştirilmiş **SepetID** sütunu tanımlandı.

#### **2. Pivot Tablo Oluşturma**  
- Kullanıcıların aldıkları hizmetler pivot tabloya dönüştürüldü.  
- Pivot tablo binary formata çevrilerek analiz için uygun hale getirildi.

#### **3. Birliktelik Kuralları**  
- **Apriori Algoritması** kullanılarak sık kullanılan hizmet birliktelikleri çıkarıldı.  
- Birliktelik kuralları **lift**, **confidence**, ve **support** metriklerine göre sıralandı.  
- Bu kurallar yardımıyla öneri sisteminin temel mantığı geliştirildi.  

#### **4. Hizmet Öneri Fonksiyonu**  
- İlgili hizmet ID'sini alarak kullanıcıya olası hizmet önerileri sunan **arl_recommender** fonksiyonu geliştirildi.  

---

### **Çıkarımlar ve Sonuçlar**  
- **En Popüler Hizmet Birliktelikleri:**  
  - Örneğin, `2_0` hizmetini alan kullanıcıların sıklıkla `3_1` hizmetini aldığı gözlemlendi.  

- **Kullanıcılar için Kişiselleştirilmiş Öneriler:**  
  - Birliktelik kuralları yardımıyla müşterilere en ilgili hizmet önerileri sunulabilir.  

- **Lift Değeri Analizi:**  
  - Yüksek lift değeri, iki hizmetin birlikte alınma olasılığının bağımsız alınma olasılığından yüksek olduğunu gösterdi.  

- **İyileştirme Potansiyeli:**  
  - Kurulan sistem, kullanıcı davranışlarını analiz etmek ve potansiyel çapraz satış stratejileri geliştirmek için kullanılabilir.  

---

### **Kullanılan Teknolojiler**  
- **Python**: Pandas, mlxtend (Apriori ve Association Rules için).  
- **Veri Görselleştirme**: Çalışmada doğrudan kullanılmadı ancak ileride görselleştirme için `seaborn` veya `matplotlib` kullanılabilir.  
- **Algoritma**: Apriori Algoritması ve Birliktelik Kuralları.

---

### **Sonuç**  
Bu proje, Armut platformunda müşteri davranışlarını anlamaya yönelik kritik bir adım olmuştur. Kullanıcıların daha iyi bir deneyim yaşaması için kişiselleştirilmiş öneriler sunulmuş, bu da müşteri memnuniyetini artırma potansiyeline sahiptir. Çalışma, özellikle çapraz satış kampanyaları oluşturma ve müşteri bağlılığını artırma konusunda önemli bir temel sağlamaktadır.


## Proje Dosyaları  

**Kod Dosyası:** [armut_arl_project.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Recommendation_Systems/armut_arl_project.py)  
