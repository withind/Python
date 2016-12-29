from urllib.request import urlopen
from bs4 import BeautifulSoup
from creat_txt import text_create
b=[]
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:
    c=str(name.get_text())
    b.append(c)
d=",".join(b)

text_create('test161129',d)
