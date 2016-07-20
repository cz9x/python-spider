# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup

url = 'https://www.piaoniu.com'
page = '/sh-all/p1'

request = urllib2.Request(url + page)
response = urllib2.urlopen(request)
result = response.read().decode('utf-8')

soup = BeautifulSoup(result, "html.parser")

count = 0
# while True:


total = soup.find('div', class_='total').getText()

print  filter(unicode.isdigit, total)


# while True:
#     request = urllib2.Request(url + page)
#     response = urllib2.urlopen(request)
#     result = response.read().decode('utf-8')
#
#     soup = BeautifulSoup(result, "html.parser")
#
#     rnt = soup.find_all('li', class_='item')
#     for item in rnt:
#         print item.find('div', class_='title').getText()
#         print item.find('div', class_='time').getText()
#         print item.find('a', class_='venue').getText()
#         print 'https://www.piaoniu.com' + item.find('a', class_='buy').get('href')
#         print item.find('div', class_=re.compile('status')).getText()
#
#     result = soup.find_all('li', class_='page')
#     for p in result:
#         if p.find('a').getText() == u'下一页':
#             print page
#             page = p.find('a').get('href')
#
#     count += 1
#
#     if count == 70:
#         break

