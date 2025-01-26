import scrapy

class DogecoinSpider(scrapy.Spider):
    name = 'dogecoin'
    start_urls = ['https://www.binance.com/dogecoin']  # Replace with the actual URL

    def parse(self, response):
        # Extract numeric data
        numeric_data = response.css('div.numeric-data::text').getall()
        with open('numeric_data.csv', 'w') as f:
            for data in numeric_data:
                f.write(f"{data}\n")

        # Extract comments
        comments = response.css('div.comment::text').getall()
        with open('comments.txt', 'w') as f:
            for comment in comments:
                f.write(f"{comment}\n")

        # Extract other content
        other_content = response.css('div.other-content::text').getall()
        with open('other_content.txt', 'w') as f:
            for content in other_content:
                f.write(f"{content}\n")
