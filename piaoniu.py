# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
from bs4 import BeautifulSoup


class PiaoNiu:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def ConMysql(self, sql):
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', use_unicode=True,
                               charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


    def getPage(self):
        try:
            url = self.baseUrl
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接失败,错误原因: ", e.reason
                return None

    def PageNum(self, Page):
        soup = BeautifulSoup(Page, "html.parser")
        pageTotal = soup.find('div', class_='total').getText()
        pageNum = filter(unicode.isdigit, pageTotal)
        return pageNum

    def getNext(self, Page):
        soup = BeautifulSoup(Page, "html.parser")
        result = soup.find_all('li', class_='page')
        for p in result:
            if p.find('a').getText() == u'下一页':
                page = p.find('a').get('href')
        return page


    def getContent(self, Page):
        soup = BeautifulSoup(Page, "html.parser")
        rtn = soup.find_all('li', class_='item')
        for item in rtn:
            title = item.find('div', class_='title').getText()
            dt = item.find('div', class_='time').getText()
            address = item.find('a', class_='venue').getText()
            url = 'https://www.piaoniu.com' + item.find('a', class_='buy').get('href')

            sql = "insert into piaoniu_page (title,dt,address,url) values ('%s','%s','%s','%s')" % (
                title, dt, address, url)
            self.ConMysql(sql)

            print item.find('div', class_='title').getText()
            print item.find('div', class_='time').getText()
            print item.find('a', class_='venue').getText()
            print 'https://www.piaoniu.com' + item.find('a', class_='buy').get('href')



baseUrl = 'https://www.piaoniu.com'
page = '/sh-all/p1'

piaoniu = PiaoNiu(baseUrl + page)

count = 0
pageNum = piaoniu.PageNum(piaoniu.getPage())

while True:
    piaoniu.getContent(piaoniu.getPage())

    piaoniu.getNext(piaoniu.getPage())

    count += count

    if count == pageNum:
        break