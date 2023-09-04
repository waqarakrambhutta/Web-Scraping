from bs4 import BeautifulSoup
import requests


url = 'https://www.ammarakram.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
tag = soup.header
atb = tag.attrs
print(atb['class'])


