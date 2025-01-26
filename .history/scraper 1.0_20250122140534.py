from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Configure Selenium WebDriver (Ensure 'chromedriver' is in your PATH or provide its path)
service = Service('/path/to/chromedriver')  # Replace with your chromedriver path
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("https://www.binance.com")

    # Wait for the content to load (adjust time if necessary)
    time.sleep(5)

    # Get the page source after JavaScript has rendered the content
    html_content = driver.page_source

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Search for 'Ethereum' in the content
    results = soup.find_all(string=lambda text: "Ethereum" in text)

    # Print the results
    if results:
        for result in results:
            print(f"Found: {result.strip()}")
    else:
        print("Ethereum not found in the HTML.")
finally:
    # Close the browser
    driver.quit()
