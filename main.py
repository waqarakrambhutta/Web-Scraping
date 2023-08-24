import requests

url = 'https://codewithmosh.com/'
r = requests.get(url)

print(r.text)