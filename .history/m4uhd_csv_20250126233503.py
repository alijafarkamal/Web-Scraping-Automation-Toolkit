from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# CSV setup
output_file = "movies_m4uhd.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])

try:
    # Configure Chrome options to connect to the debugger
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"  # Match the debug port used by Chrome

    # Attach to the existing Chrome instance
    driver = webdriver.Chrome(options=options)

    print("Connected to Chrome...")

    # Wait for the page to load (ensure the user has already navigated to the desired page)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Example: Interact with the page (adjust selectors as per your website)
    genre_dropdown = driver.find_element(By.NAME, "genre")
    genre_dropdown.click()
    action_option = driver.find_element(By.XPATH, "//select[@name='genre']/option[@value='action']")
    action_option.click()

    # Wait for results to load
    time.sleep(3)

    # Scrape data (adjust CSS selectors for your target page)
    movie_elements = driver.find_elements(By.CSS_SELECTOR, ".item > .row")
    with open(output_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for index, movie in enumerate(movie_elements, start=1):
            try:
                title = movie.find_element(By.CSS_SELECTOR, "h3").text.strip()
                year = movie.find_element(By.CSS_SELECTOR, "p.year").text.strip()
            except:
                title, year = "N/A", "N/A"
            writer.writerow([index, title, year])

    print("Scraping complete.")

finally:
    driver.quit()
