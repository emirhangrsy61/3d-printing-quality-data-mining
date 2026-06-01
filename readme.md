================================================================================
BLM308 VERİ MADENCİLİĞİ DERSİ - FİNAL PROJESİ TESLİM DOSYASI (BAHAR 2026)
================================================================================

PROJE BAŞLIĞI: 
3D Yazıcı Dilimleme Parametreleri ile Üretim Öncesi Baskı Kalitesi ve Hata Tahmini

GELİŞTİRİCİ: 
Emirhan Yılmaz (Tek Kişilik Solo Proje)

--------------------------------------------------------------------------------
1. PROJE ÖZETİ VE PROBLEM TANIMI (CRISP-DM)
--------------------------------------------------------------------------------
Bu proje, eritmeli yığma modelleme (FDM) ve reçine (SLA) teknolojilerine sahip 200'den 
fazla endüstriyel ve hobi amaçlı 3D yazıcının mekanik limitlerini ve dilimleme (slicer) 
parametrelerini analiz eden uçtan uca bir veri madenciliği çalışmasıdır.

Üretim öncesinde hatalı parametre seçimlerinden kaynaklanan bükülme (warping), nozül 
tıkanması (under-extrusion), spagetti ve aşırı ipliklenme (stringing) gibi kronik 
arıza durumları, makine öğrenmesi algoritmaları ile önceden tahmin edilmektedir. Proje 
kapsamında 12 boyutlu bir özellik matrisi (feature matrix) üzerinden sınıflandırma 
modelleri eğitilmiş ve operatörün parametreleri test edebileceği, Plotly grafik destekli 
modern bir endüstriyel kontrol paneli (Streamlit arayüzü) geliştirilmiştir.

--------------------------------------------------------------------------------
2. PROJE KLASÖR YAPISI
--------------------------------------------------------------------------------
Teslim edilen proje dizini aşağıdaki hiyerarşiye sahiptir:

baski_hata_ve_kalite_kontrol/
│
├── veri/
│   └── 3d_yazici_verisi_v2.csv      <- 6000 satırlık sentezlenmiş orijinal veri seti
│
├── kod/
│   ├── makineler.py                 <- 200+ yazıcı modeli ve mekanik sınıf tanımları
│   ├── veri_olustur.py              <- Mantıksal mühendislik kurallı veri simülatörü
│   ├── proje_pipeline.py            <- Ana DM hattı (Ön işleme, 3 model eğitimi, metrikler)
│   └── app.py                       <- Plotly grafik destekli modern Streamlit web arayüzü
│
├── README.txt                       <- Bu bilgilendirme dosyası
└── rapor.pdf                        <- LaTeX ile derlenmiş detaylı CRISP-DM proje raporu

--------------------------------------------------------------------------------
3. GEREKSİNİMLER VE KURULUM
--------------------------------------------------------------------------------
Projeyi yerel bilgisayarınızda hazır hale getirmek için Python 3.8+ sürümünün yüklü 
olması ve aşağıdaki kütüphanelerin terminal üzerinden indirilmiş olması gerekmektedir:

pip install pandas numpy scikit-learn streamlit plotly

--------------------------------------------------------------------------------
4. SİSTEMİ ÇALIŞTIRMA TALİMATLARI
--------------------------------------------------------------------------------
Süreci uçtan uca koşturmak için terminal (CMD) üzerinden "kod/" klasörünün içine giriniz:
cd kod/

Adım 1: Orijinal Veri Setinin Sentezlenmesi / Oluşturulması
-> python veri_olustur.py
(Bu komut, 'veri/' klasörü altında 6000 satırlık güncel CSV dosyasını üretecektir.)

Adım 2: Model Performanslarının ve Metriklerin Terminalde Listelenmesi
-> python proje_pipeline.py
(Lojistik Regresyon, Karar Ağacı ve Rastgele Orman modellerini eğitir; Hata Matrisini 
ve F1-Skorlarını ekrana döker.)

Adım 3: Modern Web Arayüzünün (Kalite Kontrol Paneli) Başlatılması
-> streamlit run app.py
(Komut çalıştıktan sonra tarayıcınızda http://localhost:8501 adresi otomatik açılacaktır. 
Görsel panel üzerinden 12 parametrenin tamamı anlık olarak test edilebilir.)

--------------------------------------------------------------------------------
5. PERFORMANS VE MODEL SONUÇLARI ÖZETİ
--------------------------------------------------------------------------------
Eğitim ve test verileri %80-%20 oranında (stratify korunarak) ayrılmıştır. 

* Lojistik Regresyon (Linear Baseline) : %79.70 Doğruluk (Accuracy)
* Karar Ağacı (Kural Tabanlı)         : %88.10 Doğruluk (Accuracy)
* Rastgele Orman (Ensemble)           : %88.00 Doğruluk (Accuracy)

Yorum: 3D yazıcı üretim süreçlerindeki termal kırılmalar ve hız-sıcaklık ilişkileri 
doğrusal (lineer) bir yapıda olmadığından, ağaç tabanlı modeller lineer modellere 
göre belirgin bir üstünlük sağlamıştır. Rastgele Orman modeli, hatalı baskıları 
(Sınıf 0) üretim başlamadan yakalamada %91 Duyarlılık (Recall) başarısına ulaşmıştır.

--------------------------------------------------------------------------------
6. BONUS PUAN TALEPLERİ VEYA GEREKÇELERİ
--------------------------------------------------------------------------------
Ders yönergesinin "Bonus Kuralı" maddesine dayanarak, projede gerçekleştirilen ek işler 
ve gerekçeli puan talepleri aşağıda sunulmuştur:

[+] Orijinal Veri Toplama / Sentezleme (+5 Puan): 
Literatürdeki termal/mekanik arıza dinamikleri (bükülme, akış yetersizliği, aşırı ısıda 
PLA yanması) kod tabanına dökülerek 6,000 satırlık özgün bir veri seti sentezlenmiştir.

[+] LaTeX Rapor Formatı (+5 Puan): 
Rapor şablonu standart kelime işlemciler yerine tamamen akademik LaTeX formatında 
tasarlanmış ve PDF olarak derlenmiştir.

[+] GitHub Kanal Kullanımı (+5 Puan): 
Projenin tüm kaynak kodları, veri seti ve sürüm commit geçmişi public GitHub reposu 
üzerinde paylaşılmıştır. 

[+] Demo Videosu (+3 Puan): 
Geliştirilen arayüzün ve yapay zeka modelinin dinamik parametre değişimlerine verdiği 
tepkileri içeren yerel bir ekran kaydı (demo_videosu.mp4) teslim klasörüne eklenmiştir.

[+] Hata Analizi (+2 Puan): 
Modellerin test aşamasında nerede ve neden çuvalladığı (Örn: Lojistik regresyonun non-lineer 
termal kırılmaları neden yakalayamadığı) raporda matrisler üzerinden detaylıca analiz edilmiştir.

[+] Açık Uçlu Ek İş - Streamlit Endüstriyel Kontrol Paneli (+1 ile +10 Arası Puan): 
Proje sadece terminalde çalışan bir kod olmaktan çıkarılmış; Plotly kütüphanesi ve HTML/CSS 
enjeksiyonları kullanılarak, 12 parametrenin tamamını anlık işleyen, geometrik sınır hatalarını 
ve donanım uyuşmazlıklarını (reçine cihazında filament seçilmesi gibi) operatöre dinamik 
olarak raporlayan tam teşekküllü bir web uygulamasına dönüştürülmüştür.

--------------------------------------------------------------------------------
7. YAPAY ZEKA KULLANIM BEYANI
--------------------------------------------------------------------------------
Akademik dürüstlük kuralları gereğince; bu projenin arayüz tasarımlarındaki CSS tasarım 
şablonlarında, veri yapısı optimizasyon süreçlerinde ve LaTeX doküman hiyerarşisinin 
kurulmasında büyük dil modellerinden (LLM) yardımcı araç olarak yararlanılmıştır. Projenin 
ana fikri, veri setindeki mühendislik mantık kural motorunun kurgulanması, DM modellerinin 
deneysel sonuç analizi ve endüstriyel iş değeri yorumlamaları tamamen özgün öğrenci çalışmasıdır.
================================================================================