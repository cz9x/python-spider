# -*- coding:utf-8 -*-
import re
import urllib2
import MySQLdb
from bs4 import BeautifulSoup


def mysqlInsert(sql):
    conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
                           use_unicode=True, charset="utf8")
    # conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test',
    #                        use_unicode=True, charset="utf8")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


url = 'https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.header.4.9qTGqc&n_s=new'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

soup = BeautifulSoup(response.read(), "html.parser")

# print soup
items = soup.find_all('div', class_='movie-card-wrap')
pattern = re.compile('\d+')

for item in items:
    print item.find('span', class_='bt-l').getText()
    print item.find('span', class_='bt-r').getText()
    print re.search(pattern, item.find('a').get('href')).group()

    movieName = item.find('span', class_='bt-l').getText()
    movieScore = item.find('span', class_='bt-r').getText()
    movieId = re.search(pattern, item.find('a').get('href')).group()

    detail = item.find_all('div', class_='movie-card-list')
    # print detail
    for i in detail:
        print i.find('span').getText()
        print i.find('span').find_next('span').getText()
        print i.find('span').find_next('span').find_next('span').getText()
        print i.find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next(
            'span').getText()

        movieDirector = i.find('span').getText()
        movieActor = i.find('span').find_next('span').getText()
        movieTags = i.find('span').find_next('span').find_next('span').getText()
        movieLongs = i.find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next(
            'span').getText()

    sql = "insert into tpp_movie_list (movie_id,movie_name,movie_score,movie_director,movie_actor,movie_tags,movie_longs,created_at) " \
          "values ('%s','%s','%s','%s','%s','%s','%s',now())" % \
          (movieId, movieName, movieScore, movieDirector, movieActor, movieTags, movieLongs)

    mysqlInsert(sql)

    update = "update tpp_movie_list set movie_director="