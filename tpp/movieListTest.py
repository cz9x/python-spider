# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup

url = 'https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.header.4.9qTGqc&n_s=new'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

soup = BeautifulSoup(response.read(), "html.parser")

# print soup
items = soup.find_all('div', class_='movie-card-wrap')
pattern = re.compile('\d+')

for item in items:
    print item.find('span', class_='bt-l').getText()
    print item.find('span', class_='bt-r').getText()
    print re.search(pattern, item.find('a').get('href')).group()

    detail = item.find_all('div', class_='movie-card-list')
    # print detail
    for i in detail:
        print i.find('span').getText()
        print i.find('span').find_next('span').getText()
        print i.find('span').find_next('span').find_next('span').getText()
        print i.find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').getText()