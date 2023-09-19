import requests 
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

box = soup.find_all('div',class_ ="col-sm-4 col-lg-4 col-md-4")

for i in box:
    print(i)