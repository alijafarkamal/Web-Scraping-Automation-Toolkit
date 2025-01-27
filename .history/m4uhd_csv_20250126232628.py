from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# CSV file setup
output_file = "movies_m4uhd.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])  # Write the header row

try:
    # Set up Chrome options to connect to the running instance
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"  # Connect to the debugging port

    # Create a WebDriver instance
    driver = webdriver.Chrome(options=options)

    # Switch to the already open page
    print("Connected to the existing Chrome browser...")
    
    # Ensure the page is fully loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Locate the genre dropdown and select "Action"
    genre_dropdown = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "genre"))
    )
    genre_dropdown.click()
    action_option = driver.find_element(By.XPATH, "//select[@name='genre']/option[@value='action']")
    action_option.click()
    time.sleep(3)  # Wait for the page to reload after selecting "Action"

    movie_count = 1

    while True:
        # Extract movie titles and years from the current page
        movie_elements = driver.find_elements(By.CSS_SELECTOR, ".item > .row")
        
        with open(output_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for movie in movie_elements:
                try:
                    title = movie.find_element(By.CSS_SELECTOR, "h3").text.strip()
                    year = movie.find_el
