from bs4 import BeautifulSoup
import requests


url = 'https://webscraper.io/'
r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
tag = soup.header.div.img
print(tag)

