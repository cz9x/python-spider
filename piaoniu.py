# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
from bs4 import BeautifulSoup

class PiaoNiu:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def ConMysql(self, sql):
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', use_unicode=True, charset="utf8")
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
            # return response.read().decode('utf-8')
            return response.read().decode('utf-8')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接失败,错误原因: ", e.reason
                return None


    def getContent(self, Page):
        soup = BeautifulSoup(Page, "html.parser")
        rtn = soup.find_all('li', class_='item')
        # items = []
        for item in rtn:

            # items.append(item.find('div', class_='title').getText())
            # items.append(item.find('div', class_='time').getText())
            # items.append(item.find('a', class_='venue').getText())
            # items.append('https://www.piaoniu.com' + item.find('a', class_='buy').get('href'))

            title = item.find('div', class_='title').getText()
            dt = item.find('div', class_='time').getText()
            address = item.find('a', class_='venue').getText()
            url = 'https://www.piaoniu.com' + item.find('a', class_='buy').get('href')

            sql = "insert into piaoniu_page (title,dt,address,url) values ('%s','%s','%s','%s')" % (title, dt, address, url)
            conmysql = self.ConMysql(sql)

            print item.find('div', class_='title').getText()
            print item.find('div', class_='time').getText()
            print item.find('a', class_='venue').getText()
            print 'https://www.piaoniu.com' + item.find('a', class_='buy').get('href')


baseUrl = 'http://www.piaoniu.com/sh-concerts'
piaoniu = PiaoNiu(baseUrl)

print piaoniu.getContent(piaoniu.getPage())
# print piaoniu.getPage()
