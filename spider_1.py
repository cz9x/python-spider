import urllib2

request = urllib2.Request("http://chopper2.test.zhai.me/#/login")

response = urllib2.urlopen(request)

print response.read()
# print response
