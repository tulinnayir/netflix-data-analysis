import pandas as pd
import matplotlib.pyplot as plt


#1. Veriyi Yükleme
try:
    df = pd.read_csv("netflix_titles.csv")
    print("✅ Veri başarıyla yüklendi.\n")
except FileNotFoundError:
    print("❌ Hata: 'netflix_titles.csv' dosyası bulunamadı!")
    exit()

# 2. Veriye İlk Bakış ve Temizlik
print("--- Veri Seti Özeti ---")
print(f"Toplam Satır: {df.shape[0]}, Toplam Sütun: {df.shape[1]}")
print("\nEksik Değer Kontrolü:")
print(df.isnull().sum()) # Hangi sütunda kaç tane boş veri var?

# 3. İçerik Türü Analizi (Film vs Dizi)
plt.figure(figsize=(8, 5))
plt.style.use('ggplot') #modern görünüm

type_counts = df["type"].value_counts()
type_counts.plot(kind="bar", color=['skyblue', 'salmon'])

plt.title("Netflix: Film ve Dizi Dağılımı", fontsize=14)
plt.ylabel("İçerik Sayısı")
plt.xticks(rotation=0) 
plt.show()

# 4. Ülke Bazlı Analiz (En çok içerik üreten ilk 10 ülke)
plt.figure(figsize=(10, 6))
top_countries = df["country"].value_counts().head(10)
top_countries.plot(kind="barh", color='teal') # Yatay bar grafiği daha şıktır

plt.title("En Çok İçerik Üreten İlk 10 Ülke", fontsize=14)
plt.xlabel("İçerik Sayısı")
plt.gca().invert_yaxis() # En yüksek olanı en üste getirir
plt.show()

# 5. Ekstra Analiz: Yıllara Göre Eklenen İçerik (Bonus)
# 'date_added' sütununu tarih formatına çevirip yılı çekiyoruz
df['year_added'] = pd.to_datetime(df['date_added'].str.strip()).dt.year
yearly_growth = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
yearly_growth.plot(kind="line", marker='o', color='red')
plt.title("Yıllara Göre Netflix'e Eklenen İçerik Sayısı", fontsize=14)
plt.ylabel("Eklenen İçerik")
plt.grid(True)
plt.show()