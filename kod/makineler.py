# En popüler üretim ve hobi makineleri (Arama ve kaydırma listesinde en üstte çıkacaklar)
POPULER_YAZICILAR = [
    "Bambu Lab A1 Combo", "Bambu Lab P1S", "Bambu Lab A1", "Bambu Lab X1 Carbon",
    "Bambu Lab P1S Combo", "Ender-3 V2", "Ender-3 V3 SE", "Ender-3 V3 KE", 
    "Original Prusa MK4", "Anycubic Kobra 2 Pro", "Elegoo Neptune 4 Pro", 
    "Creality K1C", "Creality K1 Max", "Bambu Lab A1 Mini Combo", "Bambu Lab A1 Mini"
]

# Kullanıcının ilettiği devasa listenin geri kalanı
DIGER_YAZICILAR = [
    "P1P", "X1", "X1 Carbon Combo", "X1E", "H2S", "H2D", "H2D Laser Edition", "H2D 10W Laser Edition", 
    "H2D 40W Laser Edition", "H2D AMS Combo", "H2D Laser AMS Combo", "H2D Pro", "X2D",
    "Ender-3", "Ender-3 Pro", "Ender-3 Neo", "Ender-3 Max", "Ender-3 Max Neo", "Ender-3 S1", "Ender-3 S1 Pro", 
    "Ender-3 S1 Plus", "Ender-3 V3", "Ender-3 V3 Plus", "Ender-3 V4", "Ender-5", "Ender-5 Pro", "Ender-5 Plus", 
    "Ender-5 S1", "Ender-5 Max", "Ender-6", "Ender-7", "CR-6 SE", "CR-6 Max", "CR-10", "CR-10 Mini", "CR-10 S4", 
    "CR-10 S5", "CR-10 Smart", "CR-10 Smart Pro", "CR-10 SE", "CR-200B", "CR-M4", "CR-5 Pro", "CR-5 Pro H", 
    "K1", "K1 SE", "K2 SE", "K2", "K2 Combo", "K2 Pro", "K2 Pro Combo", "K2 Plus", "K2 Plus Combo", 
    "Creality Hi", "Creality Hi Combo", "Sermoon D1", "Sermoon D1 Pro", "Sermoon M1", "Sermoon V1", "Sermoon V1 Pro", 
    "Sermoon S1", "Sermoon P1", "Sermoon X1", "HALOT-One", "HALOT-One Plus", "HALOT-One Pro", "HALOT-Lite", 
    "HALOT-Mage", "HALOT-Mage S", "HALOT-Mage Pro", "HALOT-SKY", "HALOT-SKY 2025", "HALOT-R6", "HALOT-X1", "HALOT-Play", 
    "LD-002H", "LD-002R", "LD-006", "LD-006H", "Kobra", "Kobra Go", "Kobra Neo", "Kobra 2", "Kobra 2 Neo", 
    "Kobra 2 Plus", "Kobra 2 Max", "Kobra 3", "Kobra 3 Combo", "Kobra 3 Max", "Kobra S1", "Kobra S1 Combo", 
    "Vyper", "Chiron", "Mega Zero", "Mega Zero 2.0", "Mega S", "Mega Pro", "Mega X", "Photon", "Photon S", 
    "Photon Mono", "Photon Mono 2", "Photon Mono 4", "Photon Mono M5", "Photon Mono M5s", "Photon Mono M5s Pro", 
    "Photon Mono X", "Photon Mono X2", "Photon Mono X6Ks", "Photon Mono X 6K", "Photon Mono X 6Ks", "Photon D2", 
    "Photon Ultra", "Photon M3", "Photon M3 Plus", "Photon M3 Max", "Photon M3 Premium", "Photon Workshop Edition", 
    "Neptune 2", "Neptune 2D", "Neptune 2S", "Neptune 3", "Neptune 3 Pro", "Neptune 3 Plus", "Neptune 3 Max", 
    "Neptune 4", "Neptune 4 Plus", "Neptune 4 Max", "Neptune X", "Mars", "Mars Pro", "Mars 2", "Mars 2 Pro", "Mars 3", 
    "Mars 3 Pro", "Mars 4", "Mars 4 Ultra", "Mars 5", "Mars 5 Ultra", "Saturn", "Saturn S", "Saturn 2", "Saturn 3", 
    "Saturn 3 Ultra", "Saturn 4", "Saturn 4 Ultra", "Jupiter", "Jupiter SE", "OrangeStorm Giga", "Centauri Carbon", 
    "Original Prusa Mini", "Original Prusa Mini+", "Original Prusa MK2", "Original Prusa MK2S", "Original Prusa MK3", 
    "Original Prusa MK3S", "Original Prusa MK3S+", "Original Prusa MK4S", "Original Prusa XL", "Original Prusa CORE One", 
    "SL1", "SL1S Speed", "X-One", "X-One2", "X-Plus", "X-Plus II", "X-Plus 3", "Plus4", "X-Max", "X-Max II", "X-Max 3", 
    "X-Smart", "X-Smart 3", "i-Fast", "Q1 Pro", "Adventurer 3", "Adventurer 3 Pro", "Adventurer 4", "Adventurer 4 Pro", 
    "Adventurer 5M", "Adventurer 5M Pro", "Creator Pro", "Creator Pro 2", "Creator 3", "Creator 4", "Guider 2", 
    "Guider 2S", "Guider 3", "Guider 3 Plus", "Guider IIS", "Dreamer", "Dreamer NX", "Finder", "Finder 3", "Foto 6.0", 
    "Foto 8.9", "Foto 9.25", "QQ-S", "QQ-S Pro", "SR", "Super Racer", "V400", "T1", "T1 Pro", "S1", "SV01", "SV01 Pro", 
    "SV02", "SV03", "SV04", "SV05", "SV06", "SV06 Plus", "SV07", "SV07 Plus", "SV08", "Sidewinder X1", "Sidewinder X2", 
    "Sidewinder X3", "Sidewinder X3 Plus", "Sidewinder X4 Plus", "Genius", "Genius Pro", "Hornet", "M1 Pro", "Voron 0", 
    "Voron 0.1", "Voron 0.2", "Voron 1", "Voron 1.5", "Voron 1.8", "Voron 2", "Voron 2.1", "Voron 2.2", "Voron 2.4", 
    "Voron Switchwire", "Voron Trident", "N1", "N2", "N2 Plus", "E2", "E2CF", "Pro2", "Pro2 Plus", "RMF500", "DF2", 
    "Form 1", "Form 1+", "Form 2", "Form 3", "Form 3+", "Form 3B", "Form 3B+", "Form 4", "Form 4B", "Fuse 1", 
    "Fuse 1+ 30W", "Form Auto", "Ultimaker Original", "Ultimaker 2", "Ultimaker 2 Extended", "Ultimaker 2+", 
    "Ultimaker 2+ Extended", "Ultimaker 3", "Ultimaker 3 Extended", "Ultimaker S3", "Ultimaker S5", "Ultimaker S7", 
    "Factor 4", "Replicator Mini", "Replicator 2", "Replicator 2X", "Replicator 5th Gen", "Replicator+", "Method", 
    "Method X", "Method XL", "Sketch", "Sketch Large", "XY-2 Pro", "X5SA", "X5SA Pro", "X5SA-400", "X5SA-500", "Moore 1", 
    "VEHO 600", "VEHO 800", "VEHO 1000", "Crux 1", "Gemini S"
]

TUM_YAZICILAR = POPULER_YAZICILAR + DIGER_YAZICILAR

# Makine türlerini sınıflandırma (Hata analizi mantığı için)
KAPALI_KASA_YAZICILAR = ["Bambu Lab P1S", "Bambu Lab X1 Carbon", "Bambu Lab P1S Combo", "Creality K1C", "Creality K1 Max", "Q1 Pro", "X-Max 3", "Adventurer 5M Pro"]
RECINE_YAZICILAR = ["Photon", "Mars", "Saturn", "Jupiter", "HALOT", "LD-", "Form", "SL1", "Foto"]

def yazici_tipini_bul(yazici_adi):
    for kelime in RECINE_YAZICILAR:
        if kelime in yazici_adi:
            return "RECINE"
    if yazici_adi in KAPALI_KASA_YAZICILAR:
        return "KAPALI_FDM"
    return "ACIK_FDM"