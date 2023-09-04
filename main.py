from bs4 import BeautifulSoup
import requests


url = 'https://codewithmosh.com/'
r = requests.get(url)

# print(r.text)

soup = BeautifulSoup(r.text,'lxml')
print(soup)


