
CRM Analitiği

    CRM Analitiği, iş dünyasında en çok uygulama alanı bulan analiz yöntemlerinden biridir. Bu süreçte Python kullanarak müşteri verilerini analiz etmeyi öğrendim ve bu sayede müşterileri daha yakından tanıyabilme, segmentlere ayırabilme ve segmentlere özel iş kararları alabilme becerisi kazandım. Ayrıca, müşterileri elde tutmaya yönelik terk modelleri geliştirme konusunda yetkinlikler edindim. Bu çalışmalar sayesinde, programlama ve veri analizi becerilerimi gerçek iş problemleriyle ilişkilendirerek pekiştirme fırsatı buldum.
    
    - Konu Başlıkları ve Detayları -

       1. CRM Analitiğine Giriş:

        Zamana dayalı çeşitli matematiksel göstergeleri inceleyerek ürün performans durumları hakkında yorum yapabilme ve temel dijital pazarlama metriklerini analiz etme becerisi edindim..
        Temel performans göstergelerini (KPI) analiz ederek ürün ve hizmetlerin performansı hakkında yorum yapmayı öğrendim.
        Kohort analizi ile zamana bağlı müşteri davranışlarını inceleyerek müşteri sadakati ve trendlerini anlamlandırma becerisi kazandım.
            
            - CRM Analitiğine Giriş
            - Temel Performans Göstergeleri
            - Kohort Analizi
    
        2.RFM Analizi:

        Müşteri satın alma davranışlarına dayalı olarak kural tabanlı segmentasyon yapmayı ve bu süreçte veri hazırlama, RFM metriklerini hesaplama ve segmentler oluşturma adımlarını başarıyla uygulamayı öğrendim.
        RFM analizini modüler bir şekilde fonksiyonlaştırarak süreçleri daha verimli hale getirebilme yetkinliği geliştirdim.

            - Veriyi Hazırlama
            - RFM Metriklerinin Hesaplanması
            - RFM Skorlarının Hesaplanması
            - RFM Segmentlerinin Oluşturulması
            - Tüm Sürecin Fonksiyonlaştırılması
    
        3.Müşteri Yaşam Boyu Değeri (Customer Lifetime Value - CLTV):

        Satın alma ve karlılık kalıplarını matematiksel ve istatistiksel modellerle analiz ederek müşteri yaşam boyu değerini hesaplama becerisi kazandım.
        Ortalama sipariş değeri, satın alma sıklığı, tekrarlama ve kaybetme oranları gibi metrikler üzerinden müşteri değeri analizi yapmayı öğrendim.
        Müşteri yaşam boyu değerine göre segmentler oluşturarak bu analizleri iş kararlarına entegre etmeyi öğrendim.

            - Veriyi Hazırlama
            - Ortalama Sipariş Değeri
            - Satın Alma Sıklığı
            - Tekrarlama Oranı ve Kaybetme Oranı
            - Kar Marjı
            - Müşteri Değeri
            - Müşteri Yaşam Boyu Değeri
            - Segmentlerin Oluşturulması
            - Tüm İşlemlerin Fonksiyonlaştırılması
    
        4.Müşteri Yaşam Boyu Değeri Tahmini:

        BG/NBD ve Gamma-Gamma modelleriyle müşteri terk ve satın alma davranışlarını modelleme becerisi kazandım.
        CLTV tahmin sürecini tüm aşamalarıyla fonksiyonlaştırarak, ölçeklenebilir bir analiz modeli geliştirebilme yetkinliği elde ettim.
        Bu yöntemleri kullanarak müşteri segmentasyonu yapmayı ve davranış kalıplarına göre stratejiler geliştirmeyi başardım.

            - BG/NBD ile Beklenen İşlem Sayısı
            - Gamma-Gamma Alt Model
            - BG/NBD ve Gamma-Gamma ile CLTV Tahmini
            - Verinin Okunması
            - Lifetime Veri Yapısının Hazırlanması
            - BG/NBD Modelinin Kurulması
            - Gamma-Gamma Modelinin Kurulması
            - BG/NBD ve Gamma-Gamma Modeli ile CLTV'nin Hesaplanması
            - Müşteri Segmentlerini Oluşturma
            - Çalışmanın Fonksiyonlaştırılması
    

PROJECT 1 :
    RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
        İş Problemi (Business Problem) :
            Bu proje, FLO müşterilerinin alışveriş davranışlarını analiz etmek ve bu davranışlara göre segmentler oluşturarak pazarlama stratejileri geliştirmek amacıyla yapılmıştır. Projede, RFM analizi yöntemi kullanılarak müşteriler segmentlere ayrılmış ve her segmente özel stratejiler belirlenmiştir.
        Proje Hedefi:
         - Müşterileri davranışlarına göre segmentlere ayırmak.
         - Her segment için farklı pazarlama stratejileri geliştirmek.
         - Şirketin müşteri ilişkilerini güçlendirmek ve gelir artışına katkı sağlamak.
        Veri Seti Hikayesi : 
            Bu veri seti, 2020 - 2021 yıllarında OmniChannel (hem online hem offline alışveriş yapan) müşterilerin alışveriş geçmişinden oluşmaktadır.
            ### **Veri Setindeki Değişkenler**
### **Veri Setindeki Değişkenler**

| **Değişken Adı**                  | **Açıklama**                                                                |
|-----------------------------------|-----------------------------------------------------------------------------|
| `master_id`                       | Eşsiz müşteri numarası                                                     |
| `order_channel`                   | Alışveriş yapılan platform (Android, iOS, Desktop, Mobile, Offline)        |
| `first_order_date`                | Müşterinin yaptığı ilk alışveriş tarihi                                    |
| `last_order_date`                 | Müşterinin yaptığı son alışveriş tarihi                                    |
| `last_order_date_online`          | Müşterinin online platformda yaptığı son alışveriş tarihi                  |
| `last_order_date_offline`         | Müşterinin offline platformda yaptığı son alışveriş tarihi                 |
| `order_num_total_ever_online`     | Müşterinin online platformda yaptığı toplam alışveriş sayısı               |
| `order_num_total_ever_offline`    | Müşterinin offline platformda yaptığı toplam alışveriş sayısı              |
| `customer_value_total_ever_online`| Müşterinin online alışverişlerde ödediği toplam ücret                      |
| `customer_value_total_ever_offline`| Müşterinin offline alışverişlerde ödediği toplam ücret                    |
| `interested_in_categories_12`    | Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi             |

RFM Analizi
        RFM analizi, müşterileri aşağıdaki üç kritere göre segmentlere ayırmak için kullanılan bir yöntemdir:
        Recency (Son Alışveriş): Müşterinin son alışverişinden bu yana geçen süre.
        Frequency (Alışveriş Sıklığı): Müşterinin toplam alışveriş sayısı.
        Monetary (Para Harcama): Müşterinin yaptığı toplam harcama miktarı.
    Proje Adımları
     1. Veri Hazırlama
        Veride eksik değer kontrolleri yapıldı.
        Tarih sütunları uygun formata çevrildi.
        Toplam alışveriş sayısı (order_num_total) ve toplam harcama (customer_value_total) hesaplandı.
    2. RFM Metriği Hesaplama
        Recency (Son Alışveriş):
        Analiz tarihi (veri setindeki en son tarih + 2 gün) ile last_order_date arasındaki fark hesaplandı.
        Frequency (Sıklık):
        Müşterinin toplam alışveriş sayısı hesaplandı.
        Monetary (Değer):
        Müşterinin toplam harcama miktarı hesaplandı.
    3. RFM Skorlarının Hesaplanması
        Recency, Frequency ve Monetary değerleri 1-5 arasında puanlanarak skorlar oluşturuldu.
        RF ve RFM skorları birleştirildi.
    4. Segmentlerin Oluşturulması
        Her müşterinin RF skoru, aşağıdaki segmentlere göre sınıflandırıldı:
### **Müşteri Segmentleri**

| **Segment Adı**       | **Açıklama**                                    |
|------------------------|------------------------------------------------|
| `hibernating`         | Etkileşimi azalmış müşteriler                  |
| `at_Risk`             | Kaybedilme riski yüksek müşteriler             |
| `cant_loose`          | Kesinlikle kaybedilmemesi gereken müşteriler   |
| `about_to_sleep`      | Uykuya geçmek üzere olan müşteriler             |
| `need_attention`      | Özel ilgi gerektiren müşteriler                |
| `loyal_customers`     | Sadık müşteriler                               |
| `promising`           | Gelecek vaat eden müşteriler                   |
| `new_customers`       | Yeni kazanılmış müşteriler                     |
| `potential_loyalists` | Potansiyel sadık müşteriler                    |
| `champions`           | En değerli ve en yüksek etkileşime sahip müşteriler |

Veri setini [flo_data_20k.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/datasets/flo_data_20k.csv) buradan inceleyebilirsiniz.

FLO Müşteri Segmentasyonu ve Pazarlama Stratejileri projesi için gerekli olan [FLO_RFM.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/FLO_RFM.py) çalışmayı buradan inceleyebilirsiniz.

PROJECT 2 :
    Proje : FLO Müşteri Yaşam Boyu Değeri (CLTV) Tahmini ve Segmentasyonu
    Veri Seti:  [flo_data_20k.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/datasets/flo_data_20k.csv) kullanılmıştır.
    Projenin Amacı:
        Müşteri verilerini analiz ederek yaşam boyu değerlerini (CLTV) tahmin etmek ve müşterileri bu değerlere göre segmentlere ayırmak. Böylece, şirketin pazarlama ve satış stratejilerini optimize ederek gelirlerini artırması ve müşteri sadakatini güçlendirmesi hedeflenmiştir.
    Kazanımlar:
        Müşteri Değer Analizi: CLTV hesaplaması sayesinde müşterilerin işletmeye sağladığı potansiyel değer tahmin edilmiştir.
        Segmentasyon ve Strateji: CLTV'ye dayalı müşteri segmentleri oluşturularak her segment için özel stratejiler önerilmiştir.
        Tahminleme Yetkinliği: BG/NBD ve Gamma-Gamma modelleri kullanılarak müşterilerin gelecekteki davranışları ve harcamaları başarılı bir şekilde tahmin edilmiştir.
        Veriye Dayalı Karar Alma: Şirket için daha verimli ve hedef odaklı pazarlama kampanyalarının planlanmasına olanak tanınmıştır.
        İş Süreçlerini Geliştirme: Müşterilere daha iyi hizmet sunulmasına ve işletmenin gelir hedeflerine ulaşmasına katkı sağlanmıştır.
  
FLO Müşteri Yaşam Boyu Değeri (CLTV) Tahmini ve Segmentasyonu projesi için gerekli olan[FLO_CLTV_Prediction.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/FLO_CLTV_Prediction.py)  çalışmayı buradan inceleyebilirsiniz. 

Özet Değerlendirme:
    Bu süreçte, müşteri analitiği üzerine çalışarak hem teorik bilgimi hem de uygulama becerilerimi geliştirdim. CRM Analitiği kapsamında veri analizi, segmentasyon, yaşam boyu değer hesaplama ve tahminleme gibi yetkinlikler kazandım. Gerçek iş problemlerini çözmek için bu bilgileri fonksiyonel ve pratik yöntemlerle uygulamayı öğrendim. Bu sayede, müşteri ilişkileri yönetiminde daha stratejik ve veri odaklı bir yaklaşım sergileyebilme becerisi edindim.