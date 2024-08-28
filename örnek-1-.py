from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/dp/B0BWK1CJQQ/?coliid=I2ZC192YBRV3S7&colid=59KX74VXBQW&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it"

# Create a Selenium webdriver
driver = webdriver.Chrome()  # Replace with your preferred browser

# Navigate to the website
driver.get(url)

# Get the HTML content
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the price element
price_whole_element = soup.find('span', {'class': 'a-price-whole'})
price_fraction_element = soup.find('span', {'class': 'a-price-fraction'})

# Get the price
if price_whole_element and price_fraction_element:
    price = price_whole_element.text.strip() + '' + price_fraction_element.text.strip()
    print(price)
else:
    print("Price not found")

# Close the webdriver
driver.quit()