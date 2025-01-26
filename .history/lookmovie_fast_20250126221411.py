from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Configure Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless
chrome_options.add_argument("--no-sandbox")  # Prevent sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Handle memory issues

# Set up WebDriver
service = Service("/usr/local/bin/chromedriver")  # Update this path
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://www.lookmovie2.to/movies/genre/action")

# CSV Setup
csv_file = "movies.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])

    page = 1
    movie_count = 1
    while True:
        print(f"Scraping Page: {page}")
        
        # Wait for movies to load
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mv-item-infor h6 a")))

        # Extract movie details
        movie_titles = driver.find_elements(By.CSS_SELECTOR, ".mv-item-infor h6 a")
        movie_years = driver.find_elements(By.CSS_SELECTOR, ".image__placeholder .year")

        for title, year in zip(movie_titles, movie_years):
            writer.writerow([movie_count, title.text.strip(), year.text.strip()])
            movie_count += 1

        # Check for the next button
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination_next")))
            next_button.click()
            page += 1
        except:
            print("No more pages to scrape.")
            break

print(f"Scraping complete. Data saved in {csv_file}.")
driver.quit()
