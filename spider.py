'''最近学习爬虫，抓取了一些妹子图，O(∩_∩)O~
该程序是抓取5页网页的图片，而且现在图片下载很慢，没有实现多线程，多线程还在学习。
'''
import re
import urllib
import urllib2
x=1
ret=r'src="(.+?\jpg)" alt' #匹配html下的以.jpg结尾的 URL

for page in range(1,6):
    pageurl="http://mm.51tietu.net/xinggan/leisi/list_49_%s.html" % page
    html=urllib.urlopen(pageurl).read()
    lists=re.findall(ret,html)
    print lists
    for pic in lists:
        urllib.urlretrieve('http://mm.51tietu.net'+pic,'%s.jpg' % x) #下载到本地
        x+=1
