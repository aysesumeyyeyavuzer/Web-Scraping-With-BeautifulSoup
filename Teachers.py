# Import necessary libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver
driver = webdriver.Chrome()  # Replace with your preferred browser
driver.get("https://muh.karabuk.edu.tr/akademikPersonel.aspx?BA=bilgisayar")

# Wait for the page to load
timeout = 10  # seconds
element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".personel-listesi"))
WebDriverWait(driver, timeout).until(element_present)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the teacher names
teacher_names = []
for row in soup.find_all('tr', class_='personel-listesi'):
    name = row.find('td', class_='isim').text.strip()
    teacher_names.append(name)

# Print the teacher names
print(teacher_names)

# Close the webdriver
driver.quit()