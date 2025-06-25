from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

# Set up the Chrome WebDriver
service = Service("/usr/local/bin/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service)

try:
    # Open the website
    driver.get("https://www.lookmovie2.to/")
    driver.maximize_window()

    # Wait for the page to load completely
    time.sleep(5)

    # Locate the "Categories" menu and hover over it
    categories_menu = driver.find_element(By.XPATH, "//li[@class='dropdown first']/a[contains(text(), 'Categories')]")
    ActionChains(driver).move_to_element(categories_menu).perform()
    time.sleep(1)  # Allow the dropdown to fully expand

    # Locate and click the "Action" category link
    action_link = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu level1 dropdownhover-bottom']//a[contains(text(), 'Action')]")
    action_link.click()  # Click on the "Action" link
    time.sleep(5)

    while True:
        # Extract movie titles from the current page
        movie_titles = driver.find_elements(By.CSS_SELECTOR, ".mv-item-infor h6 a")

        # Print all movie titles to the terminal
        for title in movie_titles:
            print(title.text)

        # Check for the "Next" button and click it if available
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination_next")
            next_button.click()
            time.sleep(5)  # Wait for the next page to load
        except:
            print("No more pages to navigate.")
            break

finally:
    driver.quit()
