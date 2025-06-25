from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the Chrome WebDriver (Make sure to specify the path to your chromedriver)
service = Service("/usr/local/bin/chromedriver")  # Update this path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("https://www.lookmovie2.to/")

    # Wait for the page to load completely
    time.sleep(5)  # Adjust the sleep duration as necessary

    # Locate the "Categories" dropdown menu
    categories_menu = driver.find_element(By.XPATH, "//li[@class='dropdown first']/a[contains(text(), 'Categories')]")

    # Hover over or click the "Categories" dropdown to reveal options
    ActionChains(driver).move_to_element(categories_menu).perform()
    time.sleep(1)  # Allow the dropdown to fully expand

    # Locate and click the "Action" category link
    action_link = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu level1 dropdownhover-bottom']//a[contains(text(), 'Action')]")
    action_link.click()  # Click on the "Action" link
    time.sleep(5)

    # Extract movie titles from the next page
    movie_titles = driver.find_elements(By.CSS_SELECTOR, ".mv-item-infor h6 a")

    # Print all movie titles to the terminal
    for title in movie_titles:
        print(title.text)
        

    # Infinite loop to prevent script from exiting
    print("Action category selected. Browser remains open.")
    while True:
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")
