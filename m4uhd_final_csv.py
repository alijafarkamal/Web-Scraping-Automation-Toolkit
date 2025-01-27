from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
chromedriver_path = "/usr/local/bin/chromedriver"

# Chrome options to attach to an existing session
chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"

# Set up the Chrome WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

print(f"Current URL: {driver.current_url}")

try:
    # Wait for the dropdown to load and be visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='genre']"))
    )

    # Locate the dropdown menu
    genre_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='genre']")

    # Use Select class to interact with the dropdown
    select = Select(genre_dropdown)
    select.select_by_value("action")  # Select the "Action" option by its value
    print("Successfully selected 'Action' from the dropdown.")

    # Wait for any potential updates to load
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Close the browser session
