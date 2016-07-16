#coding=utf-8
import re
import urllib2
from bs4 import BeautifulSoup

def getHtml(url):
    request = urllib2.Request(url)
    respones= urllib2.urlopen(request)
    html = respones.read()
    html = html.decode('unicode')
    return html


def getAnswer(html):

    reg = r'<span class="count">(.*?)</span>'
    voteCountRe = re.compile(reg)
    voteCountList = voteCountRe.findall(html)

    for voteCount in voteCountList:
        print(voteCount)

    regAnswer = r'<div class="content">(.*?)'
    answerRe = re.compile(regAnswer)
    answerList = answerRe.findall(html)
    for answer in answerList:
        print(answer)


def getAnswer2(html):
    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.titile)
    # table = soup.find_all('table',class='fzTab')

# <tr onmouseout="this.style.background=''" onmouseover="this.style.background='#fff7d8'">
#
# 		                  <td>2016067</td>
# 		                  <td>2016-06-12</td>
# 		                  <td class="redColor sz12">09</td>
# 		                  <td class="redColor sz12">13</td>
# 		                  <td class="redColor sz12">18</td>
# 		                  <td class="redColor sz12">20</td>
# 		                  <td class="redColor sz12">27</td>
# 		                  <td class="redColor sz12">31</td>
# 		                  <td class="blueColor sz12">04</td>
# 		                  <td>327,487,486</td>
# 		                  <td class="redColor sz12">5</td>
# 		                  <td>8,650,159</td>
# 		                  <td>117</td>
# 		                  <td>194,987</td>
# 		                  <td>946,443,820</td>
# 		                  </tr>

    tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"} )
    tds = tr.find_all('td')
    opennum = tds[0].get_text()
    reds = []
    for i in range(2,8):
        reds.append(tds[i].get_text())

    ##'print(reds)

    blue = tds[8].get_text()

    #print(blue)
    #把list转换为字符串:
    # (',').join(list)
    #最终输出结果格式如：2015075期开奖号码：6,11,13,19,21,32, 蓝球：4 44
    print(opennum+'期开奖号码：'+ (',').join(reds)+", 蓝球："+blue)


def getAnswer3(html):
    soup = BeautifulSoup(html, 'html.parser')

    a = soup.find_all('a',attrs={"class":"question_link","target":"_blank"})

    array1 = []
    array2 = []
    array3 = []

    for i in a:
        array1.append(i.get_text())

    #<a class="question_link" target="_blank" href="/question/29265587">如何快速成为数据分析师？</a>

    # <a class="zm-item-vote-count js-expand js-vote-count" href="javascript:;" data-bind-votecount="">7208</a>

    voteCount = soup.find_all('a',attrs={"class":"zm-item-vote-count js-expand js-vote-count","href":"javascript:;"})

    for vote in voteCount:
        array2.append(vote.get_text())
# <div class="zm-item-rich-text expandable js-collapse-body" data-resourceid="3889146" data-action="/answer/content" data-author-name="卡牌大师" data-entry-url="/question/29265587/answer/44010658">
#
# <p class="visible-expanded"><a itemprop="url" class="answer-date-link meta-item" data-tip="s$t$发布于 2015-04-06" target="_blank" href="/question/29265587/answer/44010658">编辑于 2015-11-17</a></p>
#

    answers = soup.find_all('div',attrs={"data-action":"/answer/content"})

    for answer in answers:
        array3.append(answer.get_text())

    list = []

    for i in range(1, len(array1)):
        temp = []
        temp.append(array1[i])
        temp.append(array2[i])
        temp.append(array3[i])
        list.append(temp)

    for item in list:
        print(item)

# html_doc = getHtml("http://zst.aicai.com/ssq/openInfo/")
# result = getAnswer2(html_doc)
# print(result)

for k in range(1,10):
    html = getHtml("https://www.zhihu.com/topic/19589774/top-answers?page="+str(k))
    result = getAnswer3(html)