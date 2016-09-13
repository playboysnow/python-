 # coding=utf-8
#http://www.loldytt.com/
'''将电影的网站放到一个列表中  循环取出并进行访问
找到匹配的电影链接 将链接保存到新的列表中
之后再深度去访问新列表中的链接
直到找到downurl 将downurl及电影名称 保存

做成图形界面  EXE的
'''
import urllib,urllib2
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,os,time,sys

reload(sys)
sys.setdefaultencoding('gb2312')


url="http://www.loldytt.com/"
html = urllib.urlopen(url)
bsObj = BeautifulSoup(html,'html.parser')

'''
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])
'''
mess=bsObj.find("div",{"class":"yueyph"}).findAll("a")
mess1=bsObj.find("div",{"class":"xinfenlei"}).findAll("a")
#print mess
urls=[]
print "now is getting url"
for link in mess:
	if 'href' in link.attrs:
		print (link.attrs['href'])
		urls.append(link.attrs['href'])
'''		
for l in mess1:
	if 'href' in l.attrs:
		print (l.attrs['href'])
		urls.append(l.attrs['href'])
'''
downurl=[]
print "now is visiting url"
for i in urls:
	newhtml=urllib.urlopen(i)
	page=BeautifulSoup(newhtml,'html.parser')
	try:
		#newmess=page.find("div",{"class":"con4"}).findAll(href=re.compile("thunder"))
		newmess=page.find("li",{"id":"li1_0"}).findAll("a")
		#print newmess
	except AttributeError:
		print "there is a error"
	for bt in newmess:
		if 'href' or 'text' in bt.attrs:
			print bt.attrs['href']
			c=bt.get_text()
			d=c.encode("gb2312","ignore")
			print d
			downurl.append(bt.attrs['href']     +      d)
			time.sleep(3)
bturl=set(downurl)
file=open('bt.txt','w')
print "now is saving bt" 
for durl in bturl:
	
	file.write(str(durl)+'\n')
file.close()
