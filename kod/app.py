import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from makineler import TUM_YAZICILAR, yazici_tipini_bul

# --- SAYFA VE TEMA AYARLARI ---
st.set_page_config(page_title="Akıllı 3D Üretim Paneli", layout="wide", initial_sidebar_state="collapsed")

# Görseldeki modern UI için Özel CSS Enjeksiyonu
st.markdown("""
<style>
    .stApp {
        background-color: #121212;
    }
    .basarili-kutu {
        background-color: #eef8f0;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-left: 5px solid #198754;
    }
    .hatali-kutu {
        background-color: #2b1414;
        border: 1px solid #ff4d4d;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-left: 5px solid #ff4d4d;
    }
    .geometri-kutu {
        background-color: #2b2314;
        border: 1px solid #ffaa00;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-left: 5px solid #ffaa00;
    }
    .metrik-baslik {
        text-align: center;
        color: #a0a0a0;
        font-size: 15px;
        margin-bottom: 3px;
    }
    .metrik-deger {
        text-align: center;
        color: #ffffff;
        font-size: 32px;
        font-weight: bold;
        font-family: monospace;
    }
    .section-title {
        color: #e0e0e0;
        border-bottom: 1px solid #333333;
        padding-bottom: 8px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. MODELİ HAZIRLAMA (Arka Plan - Caching ile Hızlı Çalışır) ---
@st.cache_resource
def modeli_hazirla():
    df = pd.read_csv('../veri/3d_yazici_verisi_v2.csv')
    df['Baski_Hizi'] = df['Baski_Hizi'].fillna(df['Baski_Hizi'].median())
    
    X = df.drop(['Baski_Durumu', 'Hata_Detayi'], axis=1)
    y = df['Baski_Durumu']
    
    kategorik = ['Yazici_Modeli', 'Filament_Tipi', 'Doluluk_Deseni', 'Destek_Tipi']
    X_encoded = pd.get_dummies(X, columns=kategorik, drop_first=True)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded)
    
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X_scaled, y)
    return model, scaler, X_encoded.columns

model, scaler, encoded_columns = modeli_hazirla()


# --- 2. DİNAMİK ÜST PANEL YERLEŞİMİ (Çıktı Alanları) ---
ust_grafik_alani = st.container()
ust_tavsiye_alani = st.container()
ust_metrik_alani = st.container()


# --- 3. KULLANICI GİRDİLERİ (12 Parametrenin Tamamı) ---
st.markdown('<div class="section-title">🎛️ Donanım & Donanım Çevre Ayarları</div>', unsafe_allow_html=True)
col_donanim1, col_donanim2, col_donanim3 = st.columns(3)

with col_donanim1:
    yazici_modeli = st.selectbox("Yazıcı Modeli", TUM_YAZICILAR, index=TUM_YAZICILAR.index("Bambu Lab A1"))
with col_donanim2:
    nozzle_capi = st.selectbox("Nozzle Çapı (mm)", [0.2, 0.4, 0.6, 0.8], index=1)
with col_donanim3:
    ortam_sicaklik = st.slider("Kabin İçi Ortam Sıcaklığı (°C)", 20, 60, 25)

st.markdown('<div class="section-title">🔥 Termal Ayarlar & Hız</div>', unsafe_allow_html=True)
col_termal1, col_termal2, col_termal3 = st.columns(3)

with col_termal1:
    nozzle_sicaklik = st.slider("Nozzle Sıcaklığı (°C)", 190, 300, 210, step=5)
with col_termal2:
    yatak_sicaklik = st.slider("Yatak Sıcaklığı (°C)", 40, 115, 60, step=5)
with col_termal3:
    baski_hizi = st.slider("Baskı Hızı (mm/s)", 40, 500, 100, step=10)

st.markdown('<div class="section-title">📐 Dilimleme (Slicer) & Geometri Ayarları</div>', unsafe_allow_html=True)
col_slicer1, col_slicer2, col_slicer3 = st.columns(3)

with col_slicer1:
    filament_tipi = st.selectbox("Filament Türü", ['PLA', 'PETG', 'ABS', 'TPU', 'ASA', 'Recine_UV'], index=0)
    katman_yuksekligi = st.selectbox("Katman Yüksekliği (mm)", [0.08, 0.12, 0.16, 0.20, 0.28], index=3)
with col_slicer2:
    doluluk_orani = st.slider("Doluluk Oranı (Infill %)", 5, 100, 15)
    doluluk_deseni = st.selectbox("Doluluk Deseni", ['Grid', 'Gyroid', 'Cubic', 'Lightning'], index=1)
with col_slicer3:
    destek_tipi = st.selectbox("Destek Tipi", ['Yok', 'Normal', 'Tree'], index=0)
    utuleme = st.radio("Ütüleme (Ironing) İşlemi", ["Kapalı", "Açık"], horizontal=True)

utuleme_val = 1 if utuleme == "Açık" else 0

# --- 4. YAPAY ZEKA VE MÜHENDİSLİK HESAPLAMALARI ---
yazici_tipi = yazici_tipini_bul(yazici_modeli)

# Güvenli Hız Sınırını Grafik İçin Belirleme
guvenli_hiz_limiti = 300 if "Bambu" in yazici_modeli or "K1" in yazici_modeli or "V400" in yazici_modeli else 120
if yazici_tipi == "RECINE":
    guvenli_hiz_limiti = 30 # Reçineliler için hareket hızı limitleri düşüktür

# Parametre sözlüğünü tam veri seti yapısına göre eşleme
parametre_dict = {
    'Yazici_Modeli': yazici_modeli, 'Nozzle_Capi': nozzle_capi, 'Katman_Yuksekligi': katman_yuksekligi,
    'Nozzle_Sicakligi': nozzle_sicaklik, 'Yatak_Sicakligi': yatak_sicaklik, 'Ortam_Sicakligi': ortam_sicaklik,
    'Baski_Hizi': baski_hizi, 'Filament_Tipi': filament_tipi, 'Doluluk_Orani': doluluk_orani,
    'Doluluk_Deseni': doluluk_deseni, 'Utuleme': utuleme_val, 'Destek_Tipi': destek_tipi
}

# Geometrik Hata Kontrolü (Katman yüksekliği nozzle çapından büyük olamaz)
geometrik_hata = katman_yuksekligi >= nozzle_capi

if geometrik_hata:
    risk_orani = 100
    durum_metni = "Kritik Hata"
elif yazici_tipi == "RECINE" and filament_tipi != "Recine_UV":
    risk_orani = 100
    durum_metni = "Uyuşmazlık"
else:
    # Veriyi modele göndermek için One-Hot formatına çevirme
    input_df = pd.DataFrame([parametre_dict])
    input_encoded = pd.get_dummies(input_df, columns=['Yazici_Modeli', 'Filament_Tipi', 'Doluluk_Deseni', 'Destek_Tipi'])
    input_encoded = input_encoded.reindex(columns=encoded_columns, fill_value=0)
    
    # Ölçeklendirme ve Tahmin
    input_scaled = scaler.transform(input_encoded)
    olasilik = model.predict_proba(input_scaled)[0]
    risk_orani = int(olasilik[0] * 100)
    durum_metni = "İdeal" if risk_orani < 30 else ("Kritik" if risk_orani > 65 else "Riskli")


# --- 5. SONUÇLARI ÜST KISMA YANSITMA (Anlık Güncellenir) ---

# 5.1 - Hız Limit Çubuğu (Plotly)
with ust_grafik_alani:
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['Güvenli Limit', 'Mevcut Hız'],
        x=[guvenli_hiz_limiti, baski_hizi],
        orientation='h',
        marker=dict(color=['#3b4050', '#a4c8fb']),
        text=[f"{guvenli_hiz_limiti} mm/s", f"{baski_hizi} mm/s"],
        textposition='outside',
        textfont=dict(color='#ffffff')
    ))
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=140,
        margin=dict(l=0, r=0, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=True, range=[0, 560], tickfont=dict(color='#a0a0a0')),
        yaxis=dict(showgrid=False, tickfont=dict(color='#a0a0a0'))
    )
    st.plotly_chart(fig, width='stretch', config={'displayModeBar': False})

# 5.2 - Operatör Geri Bildirim ve Çözüm Paneli
with ust_tavsiye_alani:
    if geometrik_hata:
        st.markdown(f"""
        <div class="geometri-kutu">
            <h4 style="color: #ba8b00; margin-top: 0;">🛑 Geometrik Dilimleme Hatası</h4>
            <p style="color: #ffebad; font-size: 16px;"><b>Katman Yüksekliği ({katman_yuksekligi}mm)</b>, <b>Nozzle Çapına ({nozzle_capi}mm)</b> eşit veya daha büyük olamaz!</p>
            <p style="color: #ffa500; font-size: 13px; margin-bottom: 0;">Mühendislik Çözümü: Katman yüksekliğini nozzle çapının maksimum %75'i olacak şekilde düşürün veya daha geniş bir nozzle ucu takın.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif yazici_tipi == "RECINE" and filament_tipi != "Recine_UV":
        st.markdown(f"""
        <div class="hatali-kutu">
            <h4 style="color: #ff4d4d; margin-top: 0;">🛑 Donanım & Malzeme Uyuşmazlığı</h4>
            <p style="color: #ffcccc; font-size: 16px;">Seçilen cihaz <b>SLA/Reçine</b> yapısındadır ancak eritmeli FDM filamenti (<b>{filament_tipi}</b>) seçilmiştir.</p>
            <p style="color: #ff8080; font-size: 13px; margin-bottom: 0;">Mühendislik Çözümü: Filament tipini 'Recine_UV' olarak güncelleyin veya listeden FDM tabanlı bir yazıcı modeli seçin.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif risk_orani < 30:
        st.markdown(f"""
        <div class="basarili-kutu">
            <h4 style="color: #0f5132; margin-top: 0;">🟩 Operatör Tavsiyesi: İdeal Kombinasyon</h4>
            <p style="color: #198754; font-size: 16px;">Tüm parametreler donanım altyapısı ve akış mekaniği ile tam uyumludur. Güvenle üretime başlayabilirsiniz.</p>
            <p style="color: #4caf50; font-size: 12px; margin-bottom: 0;">Makine Notu: {yazici_modeli} ({yazici_tipi}) üzerinde {filament_tipi} kalibrasyonu optimize edildi. Doluluk deseni: {doluluk_deseni}.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown(f"""
        <div class="hatali-kutu">
            <h4 style="color: #ff4d4d; margin-top: 0;">🟥 Operatör Tavsiyesi: Yüksek Üretim Riski</h4>
            <p style="color: #ffcccc; font-size: 16px;">Model, seçilen ayarlar kombinasyonunda ipliklenme, parça kalkması (warping) veya ekstrüzyon kaçırma riski tespit etti.</p>
            <p style="color: #ff8080; font-size: 13px; margin-bottom: 0;">Mühendislik Çözümü: Eğer filament {filament_tipi} ise ve makine açık kasaysa sıcaklıkları/ortam dengesini koruyun; hız {baski_hizi} mm/s için çok yüksekse nozzle sıcaklığını kademeli artırın.</p>
        </div>
        """, unsafe_allow_html=True)

# 5.3 - Risk ve Durum Kartları
with ust_metrik_alani:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown(f'<div class="metrik-baslik">Risk Skoru</div><div class="metrik-deger">% {risk_orani}</div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown(f'<div class="metrik-baslik">Durum</div><div class="metrik-deger">{durum_metni}</div>', unsafe_allow_html=True)