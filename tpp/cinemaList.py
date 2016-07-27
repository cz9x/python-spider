# -*- coding:utf-8 -*-

import re
import urllib2
import cookielib
from bs4 import BeautifulSoup
import MySQLdb


def mysqlInsert(sql):
    # conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
    #                        use_unicode=True, charset="utf8")
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test',
                           use_unicode=True, charset="utf8")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


def mysqlSelect(sql):
    conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
                           use_unicode=True, charset="utf8")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        # for row in result:
        #     city_code = row[0]
        #     return city_code
        return result

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    conn.close()


def getDistrictList(listUrl, cityid):
    filename = 'cookie.txt'

    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    result = opener.open(listUrl)
    cookie.save(ignore_discard=True, ignore_expires=True)

    targetUrl = 'https://dianying.taobao.com/ajaxCinemaList.htm?page=1&regionName=&cinemaName=&pageSize=500&pageLength=15&sortType=0&n_s=new'
    result = opener.open(targetUrl)

    soup = BeautifulSoup(result, "html.parser")
    items = soup.find_all('div', class_='detail-middle')
    pattern = re.compile('\d+')

    for item in items:
        print item.find('a').getText()
        print item.find('a').get('href')
        print item.find('span', class_='limit-address').getText()
        print re.search(pattern, item.find('a').get('href')).group()

        cinemaName = item.find('a').getText()
        cinemaId = re.search(pattern, item.find('a').get('href')).group()
        cinemaAdress = item.find('span', class_='limit-address').getText()
        cityId = cityid

        sql = "insert into tpp_cinema_list (city_id, cinema_id, cinema_name, cinema_address, created_at) " \
              "values ('%s', '%s', '%s', '%s', now())" % (cityId, cinemaId, cinemaName, cinemaAdress)
        print sql
        mysqlInsert(sql)


# url = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=610100'


sql = "select city_code from tpp_city_list"
result = mysqlSelect(sql)

for i in result:
    # print i[0]
    url = 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.12.stBZn0&n_s=new&city=' + str(i[0])
    getDistrictList(url, i[0])
