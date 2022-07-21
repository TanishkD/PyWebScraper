import pandas as pd
from bs4 import BeautifulSoup
import requests

requests = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(requests.text, features="html.parser")

#print(soup.get_text())

for i in soup.findAll("div", {"class":"quote"}):
    print((i.find("span", {"class":"text"})).text)

for j in soup.findAll("div", {"class":"quote"}):
    print((j.find("small", {"class":"author"})).text)