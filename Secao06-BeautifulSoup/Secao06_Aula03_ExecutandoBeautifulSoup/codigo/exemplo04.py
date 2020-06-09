from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/teste2.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

for link in bsObj.find_all("a"):
    print(link)