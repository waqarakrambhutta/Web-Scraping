import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"

r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text,'lxml')

table = soup.find('table',class_ = 'table table-sm table-hover screenertable')
head = table.find_all('th',class_ = '')

titles = []
for i in head:
    title = i.text
    titles.append(title)
    
df = pd.DataFrame(columns=titles)
print(df)