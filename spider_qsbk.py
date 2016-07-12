import urllib
import urllib2
import re

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    # print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
    items = re.findall(pattern, content)

    for item in items:
        print item[0], item[1], item[2]

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason




