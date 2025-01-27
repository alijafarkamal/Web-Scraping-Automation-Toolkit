from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    # Locate the "Action" option in the dropdown by its value attribute
    action_option = driver.find_element(By.CSS_SELECTOR, "option[value='action']")

    # Click the "Action" option
    action_option.click()
    print("Clicked on the 'Action' option.")

    # Wait to ensure the page responds to the selection
    time.sleep(3)

    print("Exiting script after clicking 'Action' option.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Close the browser session
