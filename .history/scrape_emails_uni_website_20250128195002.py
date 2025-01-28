from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re

def scrape_emails():

    chrome_options = Options()

    chrome_driver_path = '/usr/local/bin/chromedriver'

    # Setup the WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the website
        driver.get('https://lhr.nu.edu.pk/faculty/')

        # Get the page source
        page_source = driver.page_source

        # Refined regex to find emails
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_regex, page_source)

        # Remove duplicates
        emails = list(set(emails))

        # Write emails to a text file
        with open('emails.txt', 'w') as file:
            for email in emails:
                file.write(f'{email}\n')

        print('Emails have been written to emails.txt')

    except Exception as e:
        print('Error during scraping:', e)

    finally:
        # Quit the driver session
        driver.quit()

# Run the function
scrape_emails()

