from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up Chrome WebDriver using Service and Options
service = Service("/usr/local/bin/chromedriver")  # Update this path to your chromedriver
options = Options()
options.add_argument("--start-maximized")  # Start with a maximized browser window
options.add_argument("--disable-extensions")  # Disable browser extensions for better performance

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open LinkedIn (log in manually if required)
url = "https://www.linkedin.com/feed/"
driver.get(url)

# Allow time for the page to load completely
time.sleep(30)

# Scrape LinkedIn profiles (sample implementation)
profiles = []
try:
    elements = driver.find_elements(By.CLASS_NAME, "update-components-actor__meta")
    for elem in elements:
        try:
            # Extract name and bio
            name = elem.find_element(By.CLASS_NAME, "hoverable-link-text").text.strip()
            bio = elem.find_element(By.CLASS_NAME, "update-components-actor__description").text.strip()
            profiles.append({"Name": name, "Bio": bio})
        except Exception as e:
            print(f"Error extracting profile: {e}")
except Exception as e:
    print(f"Error finding elements: {e}")

# Save data to a CSV file
if profiles:
    df = pd.DataFrame(profiles)
    df.to_csv("linkedin_profiles.csv", index=False)
    print("Data saved to linkedin_profiles.csv")
else:
    print("No profiles found.")

# Close the browser
driver.quit()
