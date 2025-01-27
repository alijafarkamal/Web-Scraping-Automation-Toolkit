from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Set up the Chrome WebDriver (Make sure to specify the path to your chromedriver)
service = Service("/usr/local/bin/chromedriver")  # Update this path
options = Options()
# Comment out the line below if you want to see the browser for manual CAPTCHA solving
# options.add_argument("--headless")  # Run in headless mode for faster execution (optional)
driver = webdriver.Chrome(service=service, options=options)

# CSV file setup
output_file = "movies.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])  # Write the header row

try:
    # Open the website
    driver.get("https://ww2.m4uhd.tv/")
    
    # Wait for user to solve CAPTCHA manually
    print("Please solve the CAPTCHA manually...")
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("CAPTCHA solved! Proceeding...")
    
    # Wait for the page to load fully
    time.sleep(5)

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
        time.sleep(1)
        # # Extract movie titles and years from the current page
        # movie_elements = driver.find_elements(By.CSS_SELECTOR, ".item > .row")
        
        # with open(output_file, mode="a", newline="", encoding="utf-8") as file:
        #     writer = csv.writer(file)
        #     for movie in movie_elements:
        #         try:
        #             title = movie.find_element(By.CSS_SELECTOR, "h3").text.strip()
        #             year = movie.find_element(By.CSS_SELECTOR, "p.year").text.strip()
        #         except:
        #             title, year = "N/A", "N/A"

        #         # Write the movie details to the CSV file
        #         writer.writerow([movie_count, title, year])
        #         movie_count += 1

        # # Check if there is a "Next" button and click it
        # try:
        #     next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'next')]")
        #     next_button.click()
        #     print(f"Processed {movie_count} movies...")
        #     time.sleep(5)  # Wait for the next page to load
        # except:
        #     print("No more pages available.")
        #     break

finally:
    # Close the browser
    driver.quit()

print(f"Movie details have been saved to {output_file}.")
