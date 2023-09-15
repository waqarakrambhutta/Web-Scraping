import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'

r = requests.get(url)
soup= BeautifulSoup(r.text,'lxml')

price = soup.find('h4',{'class':'pull-right price'})
print(price.string)

rating = soup.find('p',{'class':'pull-right'})
print(rating.string)