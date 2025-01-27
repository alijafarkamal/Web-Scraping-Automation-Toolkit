from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
    # Locate the dropdown menu for genres
    genre_dropdown = driver.find_element_by_name("genre")
    
    # Create a Select object to interact with the dropdown menu
    select = Select(genre_dropdown)
    
    # Select the "Action" genre from the dropdown
    select.select_by_value("action")
    print("Action genre selected.")

    # Wait for the page to load after selecting (wait is important here)
    time.sleep(10)  # Adjust the wait time based on your requirements

    print("Waiting for further instructions...")
    while True:
        time.sleep(1)  # Keep the session alive and wait for user action
except KeyboardInterrupt:
    print("Script stopped by user.")
    driver.quit()  # Close the browser when stopped
