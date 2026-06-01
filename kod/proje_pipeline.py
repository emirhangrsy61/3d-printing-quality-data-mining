import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

print("--- 1. VERI SETI YUKLENIYOR ---")
try:
    df = pd.read_csv('../veri/3d_yazici_verisi.csv')
    print(f"Veri basariyla yuklendi. Toplam Satir: {df.shape[0]}, Toplam Sutun: {df.shape[1]}\n")
except FileNotFoundError:
    print("Hata: Veri dosyasi bulunamadi! Lutfen once 'veri_olustur.py' kodunu calistirin.")
    exit()

print("--- 2. ON ISLEME ADIMLARI ---")
df['Baski_Hizi'] = df['Baski_Hizi'].fillna(df['Baski_Hizi'].median())
df['Ortam_Sicakligi'] = df['Ortam_Sicakligi'].fillna(df['Ortam_Sicakligi'].median())
print("Eksik veriler medyan degerleriyle dolduruldu.\n")

X = df.drop(['Baski_Durumu', 'Hata_Detayi'], axis=1)
y = df['Baski_Durumu']

kategorik_kolonlar = ['Filament_Tipi', 'Doluluk_Deseni', 'Destek_Tipi']
X = pd.get_dummies(X, columns=kategorik_kolonlar, drop_first=True)
print(f"One-Hot Encoding sonrasi yeni sutun sayisi: {X.shape[1]}\n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Ozellik olceklendirme (StandardScaler) basariyla uygulandi.\n")

print("--- 3. MODEL EGITIMLERI BASLADI ---")
modeller = {
    "Lojistik Regresyon (Dogrusal Baseline)": LogisticRegression(max_iter=1000, C=1.0),
    "Karar Agaci (Kural Tabanli)": DecisionTreeClassifier(random_state=42, max_depth=6),
    "Rastgele Orman (Ensemble Yapi)": RandomForestClassifier(random_state=42, n_estimators=100)
}

print("--- 4. PERFORMANS METRIKLERI VE KARSILASTIRMA ---\n")
for isim, model in modeller.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"==================== {isim} ====================")
    print(f"Genel Dogruluk (Accuracy): {acc:.4f}")
    print("\nHata Matrisi (Confusion Matrix):")
    print(f"   Tahmin:0  Tahmin:1\nGercek:0  {cm[0][0]:<8}{cm[0][1]}")
    print(f"Gercek:1  {cm[1][0]:<8}{cm[1][1]}\n")
    print("Siniflandirma Raporu:")
    print(classification_report(y_test, y_pred, target_names=['Hatali Baski (0)', 'Basarili Baski (1)']))
    print("-" * 60 + "\n")