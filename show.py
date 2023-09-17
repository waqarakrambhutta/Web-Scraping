import requests
from bs4 import BeautifulSoup

url = "http://web.uaf.edu.pk/"
r = requests.get(url)

# print(r.status_code)
soup = BeautifulSoup(r.text,'lxml')

gigs = soup.find_all("p",class_= '')

print(gigs.string)


# for i in gigs:
#     print(i.string)