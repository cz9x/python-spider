# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup
from pip._vendor.requests.packages import chardet

url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.2.1.ZfsDoE&catid=50100411&st_trust=1&q=%D1%DD%B3%AA%BB%E1&ist=0&divisionId='


request = urllib2.Request(url)
response = urllib2.urlopen(request)
result = response.read().decode('GB2312')

total = BeautifulSoup(result, "html.parser")

items = total.find_all('li', class_='item-info-wrapper item-idle clearfix')

# print chardet.detect(result)
for item in items:
    print item.find('h4', class_='item-title').getText()
    print item.find('span', class_='price').getText()
    print item.find('div', class_='item-description').getText()