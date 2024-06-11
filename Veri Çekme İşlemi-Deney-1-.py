import csv
from bs4 import BeautifulSoup
from selenium import webdriver

# Chrome kullanarak bir webdriver örneği oluştur
driver = webdriver.Chrome()
# get yöntemi kullanarak web sitesine git
driver.get("https://tr.wikipedia.org/wiki/Adige_Cumhuriyeti")

# page_source özelliğini kullanarak sayfa kaynağını al
content = driver.page_source

# BeautifulSoup yapıcısını kullanarak sayfa kaynağını BeautifulSoup'a yükle
soup = BeautifulSoup(content, 'html.parser')

# Başlık
title_element = soup.find('h1', id='firstHeading')
title = title_element.text.strip()

# İçerik paragrafları
content_div = soup.find('div', class_='mw-parser-output')
content_paragraphs = content_div.find_all('p')

# Paragrafları birleştirerek içerik metnini oluşturma
content_text = '\n\n'
for paragraph in content_paragraphs:
    content_text += paragraph.text.strip() + '\n\n'

# İçerik metnindeki fazladan boşlukları temizleme
content_text = content_text.strip()

# CSV dosyasına yazdırma
with open('wiki_content.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Başlık ve içerik satırlarını yazdır
    writer.writerow(['Baslik', 'Icerik'])
    writer.writerow([title, content_text])

# Close the webdriver using the quit method
driver.quit()