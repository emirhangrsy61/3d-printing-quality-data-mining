import pandas as pd
import numpy as np
import random
import os
from makineler import TUM_YAZICILAR, POPULER_YAZICILAR, yazici_tipini_bul

os.makedirs('../veri', exist_ok=True)
np.random.seed(42)
veri_sayisi = 6000 # Makine çeşitliliği arttığı için veri sayısını 6000 yaptık

# Makinelerin veri setine dağıtılması: %70 ihtimalle popüler FDM'ler, %30 ihtimalle diğerleri seçilir.
secilen_makineler = []
for _ in range(veri_sayisi):
    if random.random() < 0.70:
        secilen_makineler.append(random.choice(POPULER_YAZICILAR))
    else:
        secilen_makineler.append(random.choice(TUM_YAZICILAR))

data = {
    'Yazici_Modeli': secilen_makineler,
    'Nozzle_Capi': np.random.choice([0.2, 0.4, 0.6, 0.8], veri_sayisi, p=[0.1, 0.6, 0.2, 0.1]),
    'Katman_Yuksekligi': np.random.choice([0.08, 0.12, 0.16, 0.20, 0.28], veri_sayisi),
    'Nozzle_Sicakligi': np.random.randint(190, 280, veri_sayisi),
    'Yatak_Sicakligi': np.random.randint(40, 115, veri_sayisi),
    'Ortam_Sicakligi': np.random.randint(20, 60, veri_sayisi),
    'Baski_Hizi': np.random.randint(40, 450, veri_sayisi), 
    'Filament_Tipi': np.random.choice(['PLA', 'PETG', 'ABS', 'TPU', 'ASA', 'Recine_UV'], veri_sayisi),
    'Doluluk_Orani': np.random.randint(5, 100, veri_sayisi),
    'Doluluk_Deseni': np.random.choice(['Grid', 'Gyroid', 'Cubic', 'Lightning'], veri_sayisi),
    'Utuleme': np.random.choice([0, 1], veri_sayisi, p=[0.7, 0.3]),
    'Destek_Tipi': np.random.choice(['Yok', 'Normal', 'Tree'], veri_sayisi, p=[0.5, 0.2, 0.3])
}

df = pd.DataFrame(data)

def baski_sonucunu_belirle(row):
    hata_turu = "Basarili"
    hata_puani = 0.0
    yazici_tipi = yazici_tipini_bul(row['Yazici_Modeli'])
    
    # 1. SLA/Reçine mantık filtresi
    if yazici_tipi == "RECINE" and row['Filament_Tipi'] != 'Recine_UV':
        hata_puani += 1.0
        hata_turu = "Hatali Malzeme (Reçine Cihazi)"

    # 2. Warping Mantığı (Açık Kasa ABS/ASA)
    if row['Filament_Tipi'] in ['ABS', 'ASA']:
        if yazici_tipi == "ACIK_FDM":
            hata_turu = "Warping (Kasa Acik)"
            hata_puani += 0.95
        elif yazici_tipi == "KAPALI_FDM" and row['Yatak_Sicakligi'] < 85:
            hata_turu = "Warping (Soguk Yatak)"
            hata_puani += 0.65

    # 3. Yetersiz Eritme (Tıkanma) Mantığı
    if row['Baski_Hizi'] > 300 and row['Nozzle_Sicakligi'] < 225:
        hata_turu = "Tikanma (Yetersiz Akis)"
        hata_puani += 0.85
        
    # --- YENİ EKLENEN KURALLAR (Senin Bulduğun Açığı Kapatıyoruz) ---
    
    # 4. Aşırı Isınma, İpliklenme ve Yanma Mantığı
    if row['Filament_Tipi'] == 'PLA' and row['Nozzle_Sicakligi'] > 235:
        hata_turu = "Ipliklenme / Yanma (Asiri Isi)"
        hata_puani += 0.95 # PLA 235 üstünde kesinlikle bozulur
    elif row['Filament_Tipi'] in ['PETG', 'TPU'] and row['Nozzle_Sicakligi'] > 260:
        hata_turu = "Asiri Ipliklenme"
        hata_puani += 0.85
        
    # 5. Mekanik Hız Sınırı ve Soğutma Yetersizliği
    # Bambu/K1 gibi makineler bile 350-400mm/s üzerinde PLA basarken soğutma yetiştiremez
    if row['Baski_Hizi'] > 350 and row['Filament_Tipi'] == 'PLA':
        hata_turu = "Sogutma Yetersizligi / Yuzey Bozulmasi"
        hata_puani += 0.70

    if hata_puani > random.random():
        return hata_turu, 0
    return "Basarili", 1

sonuclar = df.apply(baski_sonucunu_belirle, axis=1)
df['Hata_Detayi'] = [res[0] for res in sonuclar]
df['Baski_Durumu'] = [res[1] for res in sonuclar]

df.loc[df.sample(frac=0.05).index, 'Baski_Hizi'] = np.nan
df.to_csv('../veri/3d_yazici_verisi_v2.csv', index=False)
print("Devasa makine kütüphanesine sahip veri seti başarıyla oluşturuldu!")