# -*- coding:utf-8 -*-

import re
import time

page = '12天前'


def GetTime(TimeString):
    ticks = time.time()
    pattern = re.compile('\d')

    match = re.match(pattern, TimeString)

    result = [match.group(), TimeString.replace(match.group(), '')]

    if result[1] == '分钟前':
        Utime = ticks - 60 * int(result[0])
    elif result[1] == '小时前':
        Utime = ticks - 3600 * int(result[0])
    elif result[1] == '天前':
        Utime = ticks - 86400 * int(result[0])

    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(Utime))


url = 'https://dianying.taobao.com/cinemaDetail.htm?cinemaId=31697&n_s=new'

pattern = re.compile('\d+')
search = re.search(pattern, url)

print search.group()
