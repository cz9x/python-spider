import urllib2
import cookielib
from bs4 import BeautifulSoup


def getDistrictList(listUrl):
    filename = 'cookie.txt'

    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    result = opener.open(listUrl)
    cookie.save(ignore_discard=True, ignore_expires=True)

    targetUrl = 'https://dianying.taobao.com/ajaxCinemaList.htm?page=1&regionName=&cinemaName=&pageSize=500&pageLength=15&sortType=0&n_s=new'
    result = opener.open(targetUrl)

    soup = BeautifulSoup(result, "html.parser")
    items = soup.find_all('div', class_='detail-middle')

    for item in items:
        print item.find('a').getText()



url = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=610100'

getDistrictList(url)