from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
def test(func):
    start=time.clock()
    func()
    end=time.clock()
    print ('used:',end-start)
@test
def urlpost():
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page2.html")
    except HTTPError as e:
        print(e)
    else:
        if html is None:
            print("URL is over")
        else:    
            bsObj = BeautifulSoup(html.read(),"html.parser")
            print(bsObj.title)



