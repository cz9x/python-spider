# -*- coding:utf-8 -*-

import re
import urllib2
import MySQLdb
import time
from bs4 import BeautifulSoup


def GetTime(TimeString):
    ticks = time.time()
    pattern = re.compile('\d')

    match = re.match(pattern, TimeString)
    result = [match.group(), TimeString.replace(match.group(), '')]

    if result[1] == '分钟前':
        Utime = ticks - 60 * int(result[0])
    elif result[1] == '小时前':
        Utime = ticks - 3600 * int(result[0])
    elif result[1] == '天前':
        Utime = ticks - 86400 * int(result[0])

    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(Utime))



def ConMysql(sql):
    conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
                           use_unicode=True, charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def getPage(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print u"连接失败,错误原因: ", e.reason
            return None


url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.2.1.ZfsDoE&catid=50100411&st_trust=1&q=%D1%DD%B3%AA%BB%E1&ist=0&divisionId='

while True:
    result = getPage(url)

    total = BeautifulSoup(result, "html.parser")

    items = total.find_all('li', class_='item-info-wrapper item-idle clearfix')

    for item in items:
        print item.find('h4', class_='item-title').getText()
        print item.find('span', class_='price').getText()
        print item.find('div', class_='item-description').getText()
        print GetTime(item.find('span', class_='item-pub-time').getText())

        # title = item.find('h4', class_='item-title').getText()
        # price = item.find('span', class_='price').getText()
        # description = item.find('div', class_='item-description').getText()
        # publishTime = item.find('span', class_='item-pub-time').getText()


        # sql = "insert into xianyu (curdate(),title,price,description,publish_time) values ('%s','%s','%s','%s')" % (
        #     title, price, description, publishTime)
        #
        # ConMysql(sql)

    page = total.find('a', class_='paginator-next').get('href')
    url = 'http:' + page
