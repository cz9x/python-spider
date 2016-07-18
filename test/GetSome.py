# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

url = 'https://www.piaoniu.com'
page = '/sh-all/p1'

request = urllib2.Request(url + page)
response = urllib2.urlopen(request)
result = response.read().decode('utf-8')

soup = BeautifulSoup(result, "html.parser")

result = soup.find_all('li', class_='page')

for page in result:
    print page.find('a').getText()
    if page.find('a').getText() == u'下一页':
       print page.find('a').get('href')
