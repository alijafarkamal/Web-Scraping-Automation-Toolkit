from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json

# Path to your ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"  # Change this path

# Setup Selenium WebDriver with headless mode (no UI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening browser window
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Load the website
url = "https://www.binance.com"  # Replace with the URL you want to scrape
driver.get(url)

# Wait for JavaScript to load (increase sleep time if needed)
time.sleep(5)

# Get the page source after JavaScript has rendered
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find relevant data (e.g., cryptocurrency prices or names)
# Example: Searching for cryptocurrency names
crypto_data = []
for coin in soup.find_all('div', class_='coin-class'):  # Replace with actual classes/IDs from the page
    name = coin.get_text(strip=True)
    price = coin.find('span', class_='price-class').get_text(strip=True)  # Replace with actual class for price
    crypto_data.append({"name": name, "price": price})

# Save the extracted data into a file (JSON format for structured data)
output_file = "crypto_data.json"
with open(output_file, "w") as f:
    json.dump(crypto_data, f, indent=4)

# Close the browser
driver.quit()

# Print confirmation message
print(f"Data successfully scraped and saved to {output_file}")
