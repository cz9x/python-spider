# -*- coding:utf-8 -*-
import cookielib
import re
import urllib2
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
    pattern = re.compile('\d+')

    for item in items:
        print item.find('a').getText()
        print item.find('a').get('href')
        print item.find('span', class_='limit-address').getText()
        print re.search(pattern, item.find('a').get('href')).group()
        print item.find('a', class_='J_miniMap').get('data-points')
        print item.find('div', class_='middle-p-list').find_next().find_next().find_next().find_next().getText()

        gps = str(item.find('a', class_='J_miniMap').get('data-points')).split(',')
        print gps[0],gps[1]

url = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=310100'

getDistrictList(url)