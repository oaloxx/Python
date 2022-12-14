#how to get all linkes oh the website

from bs4 import BeautifulSoup
import requests
x = input("Inter the link of website:")
req = requests.get(x)
bs = BeautifulSoup(req.text , "html.parser")
for link in bs.findAll("a"):
    print(link.get("href"))