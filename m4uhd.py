from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
service = Service("/usr/local/bin/chromedriver")  # Update this path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("https://ww2.m4uhd.tv/home.html")

    # Wait for the CAPTCHA to be solved manually
    print("Please solve the CAPTCHA manually if it appears...")
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.NAME, "genre"))
    )

    # Locate the dropdown element by its name attribute
    dropdown = driver.find_element(By.NAME, "genre")

    # Wrap the element in a Select object
    select = Select(dropdown)

    # Select the "Action" option by its visible text
    select.select_by_visible_text("Action")

    # Optionally, wait to observe the action
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()
