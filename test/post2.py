# -*- coding:utf-8 -*-
import urllib
import urllib2
import json

url = 'http://webapi2.qingbh.com/manman/index.php/api/v3/recommend/recommend?platform=ios&ver=2.3.3.0002&deviceid=2F3247D8-B07F-4694-B361-9C21475A824F&channel=20001&os=9.3.2&model=iPhone&product=1&idfa=1DF6D0F3-C7E7-4EE7-9626-8FDCBB006FE6'

headers = {'Content-Type':'application/json'
           ,'Accept-Language':'zh-Hans-CN;q=1'
           ,'Accept-Encoding':'gzip, deflate'
           ,'User-Agent':'MovieTicket/2.3.3 (iPhone; iOS 9.3.2; Scale/3.00)'
           # ,'Referer':'webapi2.qingbh.com
           }

value = {'cityid':'2', 'regionname':'', 'sign':'cd27d1b1141f84790331d2ad2343fc65'}
data = urllib.urlencode(value)

request = urllib2.Request(url, data, headers=headers)
response = urllib2.urlopen(request)

def unzip(data):
    import gzip
    import StringIO
    data = StringIO.StringIO(data)
    gz = gzip.GzipFile(fileobj=data)
    data = gz.read()
    gz.close()
    return data

print response.read()
