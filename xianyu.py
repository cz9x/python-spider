# -*- coding:utf-8 -*-

import re
import urllib2
import MySQLdb
import time
from bs4 import BeautifulSoup

utime = 0

def GetTime(TimeString):
    ticks = time.time()
    pattern = re.compile('\d')

    match = re.match(pattern, TimeString)
    result = [match.group(), TimeString.replace(match.group(), '')]
    global utime
    if result[1] == u'分钟前':
        utime = ticks - 60 * int(result[0])
    elif result[1] == u'小时前':
        utime = ticks - 3600 * int(result[0])
    elif result[1] == u'天前':
        utime = ticks - 86400 * int(result[0])

    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(utime))



def ConMysql(sql):
    # conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
    #                        use_unicode=True, charset="utf8")
    conn = MySQLdb.connect(host='43.241.217.37', port=3306, user='root', passwd='data@jiefangyonggang', db='operation',
                           use_unicode=True, charset="utf8")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


def getPage(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()#.decode('GB2312')

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
        # print item.find('h4', class_='item-title').getText()
        # print item.find('em').getText()
        # print item.find('div', class_='item-description').getText()
        # print GetTime(item.find('span', class_='item-pub-time').getText())

        title = item.find('h4', class_='item-title').getText()
        price = item.find('em').getText()
        description = item.find('div', class_='item-description').getText()
        publishTime = GetTime(item.find('span', class_='item-pub-time').getText())


    sql = "insert into xianyu_spider (dt,title,price,description,publish_time) values (curdate(),'%s','%s','%s','%s')" \
            % (title, price, description, publishTime)
    print sql
    ConMysql(sql)

    page = total.find('a', class_='paginator-next').get('href')
    url = 'http:' + page
