from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/teste2.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.find_all("a"))