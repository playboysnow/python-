# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as TK
import tkMessageBox
import re,os,sys,time
import urllib
from bs4 import BeautifulSoup
#import MySQLdb
#import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('gb2312')

class windows():
	
	def __init__(self):
		self.root=Tk()
		self.root.title("电影搜索神器")
		self.root.geometry('600x400')
		self.frm=Frame(self.root)
		self.frm_L=Frame(self.frm)
		#self.frm_LL=Frame(self.frm_L)
		self.frm_R=Frame(self.frm)
		#self.frm_M=Frame(self.frm)
		Label(self.frm_L,text="全集网：").pack()
		self.stock_code_text=StringVar()
		stock_code=Entry(self.frm_L,textvariable=self.stock_code_text)
		self.stock_code_text.set("")
		stock_code.pack()
		'''
		Label(self.frm_L,text="股票名称：").pack()
		self.stock_name_text=StringVar()
		stock_name=Entry(self.frm_L,textvariable=self.stock_name_text)
		self.stock_name_text.set("")
		stock_name.pack()
		Label(self.frm_L,text="费率：").pack()
		self.stock_rate_text=StringVar()
		stock_rate=Entry(self.frm_L,textvariable=self.stock_rate_text)
		self.stock_rate_text.set("")
		stock_rate.pack()
		'''
		self.frm_L.pack()
		#self.frm_LL.pack(side=RIGHT)
		'''
		Label(self.frm_R,text="买入价位：").pack()
		self.stock_bprice_text=StringVar()
		stock_bprice=Entry(self.frm_R,textvariable=self.stock_bprice_text)
		self.stock_bprice_text.set("")
		stock_bprice.pack()
		Label(self.frm_R,text="卖出价位：").pack()
		self.stock_sprice_text=StringVar()
		stock_sprice=Entry(self.frm_R,textvariable=self.stock_sprice_text)
		self.stock_sprice_text.set("")
		stock_sprice.pack()
		
		Label(self.frm_R,text="搜索结果：").pack()
		self.stock_num_text=StringVar()
		stock_num=Entry(self.frm_R,textvariable=self.stock_num_text)
		self.stock_num_text.set("")
		stock_num.pack()
		'''
		self.frm_R.pack(side=BOTTOM)
		Button(self.frm_L,text="搜索",command=self.search).pack()
		'''
		Button(self.frm_M,text="结果",command=self.cal).pack(side=BOTTOM)
		Button(self.frm_R,text="图表分析",command=self.analysis).pack(side=BOTTOM)
		self.frm_M.pack(side=BOTTOM)
		'''
		self.frm.pack()
		
		
		
	def search(self):
		
		s_code=self.stock_code_text.get()
		url_code=urllib.unquote(s_code)
		print str(url_code),url_code
		url="http://so.loldytt.com/search.asp?keyword="+str(url_code)
		print url ,s_code
		urls=[]
		try:
	
			html = urllib.urlopen(url)
			bsObj = BeautifulSoup(html,'html.parser')
			mess=bsObj.find("div",{"class":"solb"}).findAll("a")
			print mess
			
			print "now is getting url"
			for link in mess:
				if 'href' in link.attrs:
					print (link.attrs['href'])
					urls.append(link.attrs['href'])
		except:
			print "network error"
		downurl=[]
		print "now is visiting url"
		for i in urls:
			
			newhtml=urllib.urlopen(i)
			page=BeautifulSoup(newhtml,'html.parser')
			try:
				#newmess=page.find("div",{"class":"con4"}).findAll(href=re.compile("thunder"))
				newmess=page.find("li",{"id":"li1_0"}).findAll("a")
				#print newmess
				for bt in newmess:
					if 'href' or 'text' in bt.attrs:
						print bt.attrs['href']
						c=bt.get_text()
						d=c.encode("gb2312","ignore")
						print d
						downurl.append(bt.attrs['href']     +     d)
						time.sleep(3)
			except AttributeError:
				print "there is a error"
		bturl=set(downurl)
		file=open(s_code,'w')
		print "now is saving bt" 
		for durl in bturl:
	
			file.write(str(durl)+'\n')
		file.close()
		print "all BT is saved"
	'''
	def cal(self):
		#price=self.stock_bprice_text.get()
		#print self.s_bprice
		try:
			s_code=self.stock_code_text.get()
			s_name=self.stock_name_text.get()
			s_rate=self.stock_rate_text.get()
			s_bprice=self.stock_bprice_text.get()
			s_sprice=self.stock_sprice_text.get()
			s_num=self.stock_num_text.get()
			s1=float(s_bprice)
			s2=float(s_sprice)
			s3=float(s_num)
			s4=float(s_rate)
			sum=(s2-s1)*s3-10-s2*s3*s4/10000
			string=str("您目前的盈亏为 %f" % sum)
			print "您目前的盈亏为 %f" % sum
			tkMessageBox.showinfo(title='结果',message=string)
		except:
			out=str("请确认输入的是数字而不是其他字符！！！")
			print "请确认输入的是数字而不是其他字符！！！"
			tkMessageBox.showinfo(title="警告",message=out)
	
		
	def save(self):
		try:
			s_code=self.stock_code_text.get()
			s_name=self.stock_name_text.get()
			s_rate=self.stock_rate_text.get()
			s_bprice=self.stock_bprice_text.get()
			s_sprice=self.stock_sprice_text.get()
			s_num=self.stock_num_text.get()
			s5=float(s_code)
			s6=str(s_name)
			s1=float(s_bprice)
			s2=float(s_sprice)
			s3=float(s_num)
			s4=float(s_rate)
			sum=(s2-s1)*s3-10-s2*s3*s4/10000
			string=str("您目前的盈亏为 %f" % sum)
			#print "insert into stock(code,name,b_price,s_price,num,rate,profit) values  (%f,%s,%f,%f,%f,%f,%f)" % (s5,repr(s6),s1,s2,s3,s4,sum)
			#print s1,s2,s3,s4,s5,s_code,s6,s_name 
			
			#print "您目前的盈亏为 %f" % sum
			tkMessageBox.showinfo(title='结果',message=string)
			
			try:
				save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
				#save=MySQLdb.connect(host='rm-bp12a3q2p8q14i0yk.mysql.rds.aliyuncs.com',user='re5sh0bjj8',passwd='Mysqlweb20',db='re5sh0bjj8')
				#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
			except Exception,e:
				print e
				sys.exit()
	
			cursor=save.cursor()
			action="insert into stock(code,name,b_price,s_price,num,rate,profit) values (%f,%s,%f,%f,%f,%f,%f)" % (s5,repr(s6),s1,s2,s3,s4,sum)
		#	action="insert into stock(code,name,b_price,s_price,num,rate,profit) values (%f,%s,%f,%f,%f,%f,%f)" % (s5,s6,s1,s2,s3,s4,sum)
		#	action1="insert into aliyun_stock(code,name,b_price,s_price,num,rate,profit) values ("+s5+","+s6+","+s1+","+s2+","+s3+","+s4+","+sum+" )"
			try:
				cursor.execute(action)
			except Exception,e:
				print e
			cursor.close()
			save.commit()
			save.close()
		except:
			out=str("请确认输入的是数字而不是其他字符！！！")
			print "请确认输入的是数字而不是其他字符！！！"
			tkMessageBox.showinfo(title="警告",message=out)

	def analysis(self):
		try:
			save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
			#save=MySQLdb.connect(host='rm-bp12a3q2p8q14i0yk.mysql.rds.aliyuncs.com',user='re5sh0bjj8',passwd='Mysqlweb20',db='re5sh0bjj8')
			#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
		except Exception,e:
			print e
			sys.exit()
	
		cursor=save.cursor()
		
		action="select id,profit from stock"
		try:
			cursor.execute(action)
		except Exception,e:
			print e
		num=cursor.fetchall()
		cursor.close()
		save.commit()
		save.close()
		x=[]
		y=[]
		i=0
		while i>=0:
			try:
				a=num[i][0]
				print a
				b=num[i][1]
				print b
				x.append(a)
				y.append(b)
				i+=1
			except IndexError:
				break
			print x,y

		plt.plot(x,y)
		plt.show()
	'''

if __name__=="__main__":
	d=windows()
	mainloop()