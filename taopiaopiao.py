# -*- coding:utf-8 -*-

import urllib2

url = 'https://dianying.taobao.com/showDetail.htm?spm=a1z21.6646385.w1.4.dA1wsj&showId=151815&source=&n_s=new'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

print response.read()

