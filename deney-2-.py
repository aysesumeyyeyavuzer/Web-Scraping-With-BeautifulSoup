from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
from bs4 import BeautifulSoup

# Selenium ile Web Sayfasını Aç ve Verileri Çek
# WebDriver'ı başlat (ChromeDriver)
driver_path = 'C:/chromedriver-win64/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Kandilli Rasathanesi deprem verileri sayfasına git
url = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'
driver.get(url)

# Sayfanın yüklenmesini bekle
time.sleep(5)  # Alternatif olarak WebDriverWait kullanabilirsiniz

# Sayfa kaynağını al
html = driver.page_source
driver.quit()

# BeautifulSoup ile sayfa kaynağını parse et
soup = BeautifulSoup(html, 'html.parser')

# Verileri Parse Et
# Verilerin bulunduğu tabloyu bul
table = soup.find('pre').text

# Satırlara ayır
rows = table.splitlines()[6:]  # İlk 6 satırı atlayın, çünkü başlık bilgisi olabilir

# Her satırı sütunlara ayır ve verileri sakla
data = []
for row in rows:
    cols = row.split()
    if len(cols) >= 9:  # En az 9 sütun olması gerekiyor
        tarih = cols[0]
        zaman = cols[1]
        enlem = cols[2]
        boylam = cols[3]
        derinlik = cols[4]
        büyüklük = cols[6]
        yer = ' '.join(cols[8:])  # Yer bilgisi birden fazla kelime olabilir
        data.append([tarih, zaman, enlem, boylam, derinlik, büyüklük, yer])

# Veriyi pandas DataFrame'e dönüştür
columns = ['Tarih', 'Zaman', 'Enlem', 'Boylam', 'Derinlik', 'Büyüklük', 'Yer']
df = pd.DataFrame(data, columns=columns)

# Verileri Excel Dosyasına Kaydet
# DataFrame'i Excel dosyasına kaydet
output_file = 'deprem_verileri.xlsx'
df.to_excel(output_file, index=False)

print(f"Veriler '{output_file}' dosyasına kaydedildi.")
