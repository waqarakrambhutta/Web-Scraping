import requests
from bs4 import BeautifulSoup
import re

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

data = soup.find_all(string=re.compile('Tab'))

for i in data:
    print(i.string)