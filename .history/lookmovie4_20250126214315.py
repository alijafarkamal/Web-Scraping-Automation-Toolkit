from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up the Chrome WebDriver (Make sure to specify the path to your chromedriver)
service = Service("/usr/local/bin/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("https://www.lookmovie2.to/")

    # Wait for the page to load completely
    time.sleep(5)  # Adjust the sleep duration as necessary

    # Find the "Categories" dropdown menu and hover over it
    categories = driver.find_element(By.LINK_TEXT, "Categories")
    categories.click()

    # Wait for the dropdown to appear
    time.sleep(2)

    # Find and click on the "Action" category link
    action_link = driver.find_element(By.LINK_TEXT, "Action")
    action_link.click()

    # Wait for the next page to load
    time.sleep(5)

    # Extract movie titles from the next page
    movie_titles = driver.find_elements(By.CSS_SELECTOR, ".mv-item-infor h6 a")

    # Print all movie titles to the terminal
    for title in movie_titles:
        print(title.text)

    # Keep the browser open
    while True:
        time.sleep(1)

finally:
    # Do not close the browser
    pass
