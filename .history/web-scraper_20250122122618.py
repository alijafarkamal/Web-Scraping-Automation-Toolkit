import requests
from bs4 import BeautifulSoup
url = 'https://www.bbc.co.uk/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))