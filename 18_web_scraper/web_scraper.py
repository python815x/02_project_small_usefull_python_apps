import requests
from bs4 import BeautifulSoup

url = 'https://www.myfxbook.com/community/outlook'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

name = soup.findall('tr', {'class': 'outlook-symbol-row'})

