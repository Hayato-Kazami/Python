from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.bilibli.com/')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)