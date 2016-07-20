# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
from pprint import pprint

url = 'http://wx.wepiao.com/cgi/movie/list'

headers = {'X-Requested-With': 'XMLHttpRequest'
         ,'Accept-Language':'zh-cn'
         ,'Accept-Encoding':'gzip, deflate'
         ,'Content-Type':'application/x-www-form-urlencoded'
         ,'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.3.22 NetType/WIFI Language/zh_CN'
         ,'Referer':'http://wx.wepiao.com/index.html?showwxpaytitle=1&channel=wxmovie'}

value = {'page':'1', 'num':'12', 'cityId':'73'}
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

# print unzip(response.read()).decode("unicode_escape").replace('')
# result = unzip(response.read()).decode("unicode_escape")


i = json.loads(unzip(response.read()).decode('utf-8'))

print i

print i['list'][0]['detail']