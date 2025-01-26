from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Path to your ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"  # Ensure the correct path to chromedriver

# Setup Selenium WebDriver with headless mode (no UI)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening browser window
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Load the website
url = "https://www.binance.com"  # Replace with the URL you want to scrape
driver.get(url)

# Wait for the page content to load using explicit waits (e.g., for the crypto table to load)
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1ap5wfn')))
except:
    print("Timed out waiting for page to load")
    driver.quit()
    exit()

# Now that the page is fully loaded, get the page source
html_content = driver.page_source

# Extract cryptocurrency data directly using Selenium WebDriver
crypto_data = []

# Use XPath or CSS selectors to get the necessary data
coins = driver.find_elements(By.XPATH, '//div[@class="css-1ap5wfn"]')  # Example for crypto rows

for coin in coins:
    try:
        # Extract name and price (you need to adjust these based on actual page structure)
        name = coin.find_element(By.XPATH, './/span[contains(@class, "css-1ap5wfn")]').text  # Adjust to correct name element
        price = coin.find_element(By.XPATH, './/span[contains(@class, "css-16ql5wq")]').text  # Adjust to correct price element

        # Add extracted data to list
        crypto_data.append({"name": name, "price": price})
    except Exception as e:
        print(f"Error extracting data: {e}")

# Save the extracted data into a JSON file
output_file = "crypto_data.json"
with open(output_file, "w") as f:
    json.dump(crypto_data, f, indent=4)

# Close the browser
driver.quit()

# Print confirmation message
print(f"Data successfully scraped and saved to {output_file}")
