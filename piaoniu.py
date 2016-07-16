# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

class PiaoNiu:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl


    def getPage(self):
        try:
            url = self.baseUrl
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # return response.read().decode('utf-8')
            return type(response.read().decode('utf-8'))

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接失败,错误原因: ", e.reason
                return None


    def getContent(self, Page):
        soup = BeautifulSoup(Page, "html.parser")
        print soup.findAll("li", class_="item")



baseUrl = 'http://www.piaoniu.com/sh-concerts'
piaoniu = PiaoNiu(baseUrl)

# print piaoniu.getContent(piaoniu.getPage())
print piaoniu.getPage()
