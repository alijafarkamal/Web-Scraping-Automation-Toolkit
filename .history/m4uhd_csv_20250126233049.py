from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# CSV file setup
output_file = "movies_m4uhd.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])  # Write the header row

try:
    # Set up Chrome options to connect to the existing browser instance
    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:9222"  # Connect to the debugging port

    # Connect to the existing Chrome instance
    driver = webdriver.Chrome(options=options)

    # Ensure the page is already open
    print("Connected to the existing Chrome browser...")

    # Wait until the page content is loaded
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
                    year = movie.find_element(By.CSS_SELECTOR, "p.year").text.strip()
                except:
                    title, year = "N/A", "N/A"

                # Write the movie details to the CSV file
                writer.writerow([movie_count, title, year])
                movie_count += 1

        # Check if there is a "Next" button and click it
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'next')]")
            next_button.click()
            print(f"Processed {movie_count} movies...")
            time.sleep(5)  # Wait for the next page to load
        except:
            print("No more pages available.")
            break

finally:
    driver.quit()

print(f"Movie details have been saved to {output_file}.")
