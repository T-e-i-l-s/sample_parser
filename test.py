# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://www.lazada.com.my/#'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

print(quotes)