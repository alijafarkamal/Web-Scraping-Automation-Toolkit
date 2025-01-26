# import scrapy

# class DogecoinSpider(scrapy.Spider):
#     name = 'dogecoin'
#     start_urls = ['https://www.binance.com/en/dogecoin']  # Replace with the actual URL

#     custom_settings = {
#         'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'ROBOTSTXT_OBEY': False
#     }

#     def parse(self, response):
#         # Extract numeric data
#         numeric_data = response.css('div.numeric-data::text').getall()
#         with open('numeric_data.csv', 'w') as f:
#             for data in numeric_data:
#                 f.write(f"{data}\n")

#         # Extract comments
#         comments = response.css('div.comment::text').getall()
#         with open('comments.txt', 'w') as f:
#             for comment in comments:
#                 f.write(f"{comment}\n")

#         # Extract other content
#         other_content = response.css('div.other-content::text').getall()
#         with open('other_content.txt', 'w') as f:
#             for content in other_content:
#                 f.write(f"{content}\n")


# import scrapy
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from scrapy.selector import Selector
# import time

# class DogecoinSpider(scrapy.Spider):
#     name = 'dogecoin'
#     start_urls = ['https://www.binance.com/en/dogecoin']

#     custom_settings = {
#         'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'ROBOTSTXT_OBEY': False
#     }

#     def __init__(self, *args, **kwargs):
#         super(DogecoinSpider, self).__init__(*args, **kwargs)
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--no-sandbox")
#         self.driver = webdriver.Chrome(options=chrome_options)

#     def parse(self, response):
#         self.driver.get(response.url)
#         time.sleep(5)  # Wait for the page to fully load

#         sel = Selector(text=self.driver.page_source)

#         # Extract numeric data
#         numeric_data = sel.css('div.numeric-data::text').getall()
#         with open('numeric_data.csv', 'w') as f:
#             for data in numeric_data:
#                 f.write(f"{data}\n")

#         # Extract comments
#         comments = sel.css('div.comment::text').getall()
#         with open('comments.txt', 'w') as f:
#             for comment in comments:
#                 f.write(f"{comment}\n")

#         # Extract other content
#         other_content = sel.css('div.other-content::text').getall()
#         with open('other_content.txt', 'w') as f:
#             for content in other_content:
#                 f.write(f"{content}\n")

#         self.driver.quit()



import requests

url = "https://www.binance.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# Send a request
response = requests.get(url, headers=headers)

# Check the response
print("Status Code:", response.status_code)
if "captcha" in response.text.lower():
    print("The website uses CAPTCHA to prevent scraping.")
elif response.status_code == 403:
    print("Access forbidden. The website likely has anti-scraping mechanisms.")
else:
    print("The website is accessible. Check for further protections.")
