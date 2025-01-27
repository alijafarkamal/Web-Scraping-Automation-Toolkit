from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
    # Locate the dropdown menu for genres using its name attribute
    genre_dropdown = driver.find_element(By.NAME, "genre")
    
    # Create a Select object to interact with the dropdown menu
    select = Select(genre_dropdown)
    
    # Select the "Action" genre from the dropdown
    select.select_by_value("action")
    print("Action genre selected.")

    # Wait to ensure the page responds to the selection
    time.sleep(3)

    print("Exiting script after selecting 'Action' genre.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Close the browser session
