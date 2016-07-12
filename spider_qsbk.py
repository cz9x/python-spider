# coding=utf-8

import urllib
import urllib2
import re
import MySQLdb

from MySQLdb import OperationalError

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
    use_unicode=1,
    charset='utf8'
)
conn.ping(True)
cur = conn.cursor()

sql = "insert into qsbk values(%s, %s, %s)"

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</', re.S)
    items = re.findall(pattern, content)

    for item in items:
        # print item[0], item[1], item[2]
        # cur.executemany(sql, (item[0], item[1], item[2]))
        cur.execute("insert into qsbk values('"+ item[0].replace('\n','') + "','" + item[1].replace('\n','') + "'," + item[2].replace('\n','') + ")")
        # print "insert into qsbk values('"+ item[0].replace('\n','') + "','" + item[1].replace('\n','') + "'," + item[2].replace('\n','') + ")"

        # cur.execute("insert into qsbk values('  123  ','  123  ', 123  )")

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

cur.close()
conn.commit()
conn.close()
