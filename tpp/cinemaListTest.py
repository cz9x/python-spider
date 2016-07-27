# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

SHurl = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=310100'
BJurl = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=110100'
SZurl = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=440300'

SHrequest = urllib2.Request(SHurl)
SHresponse = urllib2.urlopen(SHrequest)

SHsoup = BeautifulSoup(SHresponse.read(), "html.parser")

# SHresult = SHsoup.find_all('div', class_='middle-hd')
# print SHresult
# for item in SHresult:
#     print item.find('a').getText()

SHnext = SHsoup.find('div', class_='sortbar-more J_cinemaMore').get('data-ajax')
SHparam = SHsoup.find('div', class_='sortbar-more J_cinemaMore').get('data-param')
SHnextUrl = SHnext + '?' + str(SHparam).replace('10', '100')

SHnextSoup = BeautifulSoup(urllib2.urlopen(urllib2.Request(SHnextUrl)), "html.parser")
print SHnextSoup




BJrequest = urllib2.Request(BJurl)
BJresponse = urllib2.urlopen(BJrequest)

BJsoup = BeautifulSoup(BJresponse.read(), "html.parser")
#
# BJresult = BJsoup.find_all('div', class_='middle-hd')
# for item in BJresult:
#     print item.find('a').getText()

BJnext = SHsoup.find('div', class_='sortbar-more J_cinemaMore').get('data-ajax')
BJparam = SHsoup.find('div', class_='sortbar-more J_cinemaMore').get('data-param')
BJnextUrl = BJnext + '?' + str(BJparam).replace('10', '100')

BJnextSoup = BeautifulSoup(urllib2.urlopen(urllib2.Request(BJnextUrl)), "html.parser")
print BJnextSoup



# SZrequest = urllib2.Request(SZurl)
# SZresponse = urllib2.urlopen(SZrequest)
#
# SZsoup = BeautifulSoup(SZresponse.read(), "html.parser")
#
# SZresult = SZsoup.find_all('div', class_='middle-hd')
#
# for item in SZresult:
#     print item.find('a').getText()