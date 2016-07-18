# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

url = 'https://www.piaoniu.com'
page = '/sh-all/p1'

while True:

    request = urllib2.Request(url + page)
    response = urllib2.urlopen(request)
    result = response.read().decode('utf-8')

    soup = BeautifulSoup(result, "html.parser")

    rtn = soup.find_all('li', class_='item')
    for item in rtn:
        print item.find('div', class_='title').getText()
        print item.find('div', class_='time').getText()
        print item.find('a', class_='venue').getText()
        print item.find('a',class_='buy').get('href')

    if soup.find(re.compile("下一页")):
        page = soup.get('href')
        print page

    break
    # else:
    #     return False