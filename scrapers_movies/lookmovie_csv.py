from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

# Set up the Chrome WebDriver (Make sure to specify the path to your chromedriver)
service = Service("/usr/local/bin/chromedriver")  # Update this path
options = Options()
options.add_argument("--headless")  # Run in headless mode for faster execution (optional)
driver = webdriver.Chrome(service=service, options=options)

# CSV file setup
output_file = "movies.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No.", "Film Name", "Year"])  # Write the header row

try:
    # Open the website
    driver.get("https://www.lookmovie2.to/")

    # Hover over the "Categories" menu
    categories_menu = driver.find_element(By.XPATH, "//li[@class='dropdown first']/a[contains(text(), 'Categories')]")
    ActionChains(driver).move_to_element(categories_menu).perform()
    time.sleep(1)  # Allow the dropdown to fully expand

    # Locate and click the "Action" category link
    action_link = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu level1 dropdownhover-bottom']//a[contains(text(), 'Action')]")
    action_link.click()  # Click on the "Action" link
    time.sleep(5)

    movie_count = 1
    
    while True:
        # Extract movie titles and years from the current page
        movie_elements = driver.find_elements(By.CSS_SELECTOR, ".movie-item-style-2")
        
        with open(output_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for movie in movie_elements:
                title_element = movie.find_element(By.CSS_SELECTOR, ".mv-item-infor h6 a")
                title = title_element.text.strip()
                
                try:
                    year_element = movie.find_element(By.CSS_SELECTOR, "p.year")
                    year = year_element.text.strip()
                except:
                    year = "N/A"

                # Write the movie details to the CSV file
                writer.writerow([movie_count, title, year])
                movie_count += 1

        # Check if there is a "Next" button and click it
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination_next")
            next_button.click()
            print(movie_count)
            time.sleep(5)  # Wait for the next page to load
            
        except:
            print("No more pages available.")
            break

finally:
    # Close the browser
    driver.quit()

print(f"Movie details have been saved to {output_file}.")






















# pkill -f chrome
# google-chrome --remote-debugging-port=9222
# google-chrome --remote-debugging-port=9222

# curl http://127.0.0.1:9222/json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
chromedriver_path = "/usr/local/bin/chromedriver"

# Chrome options to attach to an existing session
chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"

# Set up the Chrome WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Confirm the current URL
current_url = driver.current_url
print(f"Current URL: {current_url}")

try:
    # Ensure the script is running on the desired page
    if "http" not in current_url:
        raise Exception("The browser is not on a valid webpage. Ensure the correct tab is active.")

    # Wait for the dropdown to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='genre']"))
    )

    # Locate and interact with the dropdown
    genre_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='genre']")
    select = Select(genre_dropdown)
    select.select_by_value("action")
    print("Successfully selected 'Action' from the dropdown.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

