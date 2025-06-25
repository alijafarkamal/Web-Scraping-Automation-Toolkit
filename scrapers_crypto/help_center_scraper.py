import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuration - UPDATE THESE VALUES BASED ON YOUR WEBSITE STRUCTURE
BASE_URL = "https://example.com/help-center"
CATEGORY_SELECTOR = ".category-list a"  # Selector for category links
ARTICLE_SELECTOR = ".article-list a"  # Selector for article links
TITLE_SELECTOR = "h1.article-title"  # Selector for article title
CONTENT_SELECTOR = "div.article-body"  # Selector for main content
NAV_WAIT_TIME = 3  # Seconds to wait for page loads

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Remove for visible browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def get_page_content(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, CONTENT_SELECTOR))
    )
    time.sleep(NAV_WAIT_TIME)  # Allow dynamic content to load
    return BeautifulSoup(driver.page_source, "html.parser")

def extract_content(soup):
    # Extract text content with proper formatting
    content_element = soup.select_one(CONTENT_SELECTOR)
    if not content_element:
        return ""
    
    # Handle lists and paragraphs
    for elem in content_element.find_all(["ul", "ol"]):
        for li in elem.find_all("li"):
            li.insert_before("- ")  # Markdown-style list formatting
    
    # Handle images with descriptions
    for img in content_element.find_all("img"):
        alt_text = img.get("alt", "No description")
        img.replace_with(f"\n[Image: {img['src']} - {alt_text}]\n")
    
    return content_element.get_text(separator="\n", strip=True)

def scrape_help_center():
    driver = setup_driver()
    soup = get_page_content(driver, BASE_URL)
    
    categories = []
    for cat in soup.select(CATEGORY_SELECTOR):
        categories.append({
            "name": cat.text.strip(),
            "url": cat["href"]
        })
    
    articles = []
    for category in categories:
        cat_soup = get_page_content(driver, category["url"])
        
        for article in cat_soup.select(ARTICLE_SELECTOR):
            article_url = article["href"]
            article_soup = get_page_content(driver, article_url)
            
            articles.append({
                "Category": category["name"],
                "Title": article_soup.select_one(TITLE_SELECTOR).text.strip(),
                "Content": extract_content(article_soup),
                "URL": article_url
            })
    
    driver.quit()
    return articles

def save_output(data):
    # Save to CSV
    with open("help_center.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Category", "Title", "Content", "URL"])
        writer.writeheader()
        writer.writerows(data)
    
    # Convert to JSON
    with open("help_center.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    scraped_data = scrape_help_center()
    save_output(scraped_data)
    print(f"Scraped {len(scraped_data)} articles. Files saved: help_center.csv & help_center.json")