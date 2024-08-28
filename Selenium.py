from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up options for headless Chrome
options = Options()
options.headless = True  # Enable headless mode for invisible operation
options.add_argument("--window-size=1920,1200")  # Define the window size of the browser

# Set the path to the Chromedriver
DRIVER_PATH = '/path/to/chromedriver'

# Initialize Chrome with the specified options
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Navigate to the Nintendo website
driver.get("https://www.nintendo.com/")

# Output the page source to the console
print(driver.page_source)

# Close the browser session cleanly to free up system resources
driver.quit()