import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

product = soup.find_all('a', class_ = 'title')
product_list = []
for i in product:
    prod = i.text 
    product_list.append(prod)
    
price = soup.find_all('h4', class_ = "pull-right price")
price_list = []
for i in price:
    pri = i.text 
    price_list.append(pri)
    
desc = soup.find_all('p',class_ = 'description')
desc_list = []
for i in desc:
    description = i.text    
    desc_list.append(description)

reviews = soup.find_all('p',class_ = 'pull-right')
reviews_list = []
for i in reviews:
    rew = i.text    
    reviews_list.append(rew)
    
df = pd.DataFrame({"Products":product_list,'Price':price_list,'Description':desc_list,"Reviews":reviews_list})

df.to_csv('Product_details.csv')