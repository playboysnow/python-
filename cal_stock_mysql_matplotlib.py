# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import re,os,sys
import MySQLdb
import matplotlib.pyplot as plt
root=Tk()
root.title("盈亏表")
root.geometry('600x400')
'''
#connect mysql
try:
	save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
	#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
except Exception,e:
	print e
	sys.exit()
	
cursor=save.cursor()
#cursor.execute('insert into stock(b_price,s_price,num,profit) values  (1,2,100.0,20)')
#cursor.execute("grant all on *.* to 'root'@'10.2.48.100'")
'''
#make windows
text1=Label(root,text="买入价位：")
text1.pack()
t1_text=StringVar()
t1=Entry(root,textvariable=t1_text)
t1_text.set("")
t1.pack()

text2=Label(root,text="卖出价位：")
text2.pack()
t2_text=StringVar()
t2=Entry(root,textvariable=t2_text)
t2_text.set("")
t2.pack()

text3=Label(root,text="交易总量：")
text3.pack()
t3_text=StringVar()
t3=Entry(root,textvariable=t3_text)
t3_text.set("")
t3.pack()

text4=Label(root,text="费率(万分之2.5 请填写2.5)：")
text4.pack()
t4_text=StringVar()
t4=Entry(root,textvariable=t4_text)
t4_text.set("")
t4.pack()

def click():
	try:
		t1=t1_text.get()
		t2=t2_text.get()
		t3=t3_text.get()
		t4=t4_text.get()
		a1=float(t1)
		a2=float(t2)
		a3=float(t3)
		a4=float(t4)
#		num=a1+(float(a2)-1)*a3
#		sum=(a1+num)/2*a2
		sum=(a2-a1)*a3
		string=str("您目前的盈亏为 %f" % sum)
		print "您目前的盈亏为 %f" % sum
		tkMessageBox.showinfo(title='结果',message=string)
		try:
			save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
			#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
		except Exception,e:
			print e
			sys.exit()
	
		cursor=save.cursor()
		action="insert into n_stock(b_price,s_price,num,profit) values (%f,%f,%f,%f)" % (a1,a2,a3,sum)
		try:
			cursor.execute(action)
		except Exception,e:
			print e
		cursor.close()
		save.close()
	except:
		out=str("请确认输入的是数字而不是其他字符！！！")
		print "请确认输入的是数字而不是其他字符！！！"
		tkMessageBox.showinfo(title="警告",message=out)
	
def dex():
	try:
		t1=t1_text.get()
		t2=t2_text.get()
		t3=t3_text.get()
		t4=t4_text.get()
		a1=float(t1)
		a2=float(t2)
		a3=float(t3)
		a4=float(t4)
#		num=a1+(float(a2)-1)*a3
#		sum=(a1+num)/2*a2
		sum=(a2-a1)*a3-10-a2*a3*a4/10000
		string=str("您目前的盈亏为 %f" % sum)
		print "您目前的盈亏为 %f" % sum
		tkMessageBox.showinfo(title='结果',message=string)
		
		try:
			save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
			#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
		except Exception,e:
			print e
			sys.exit()
	
		cursor=save.cursor()
		
		action="insert into stock(b_price,s_price,num,rate,profit) values (%f,%f,%f,%f,%f)" % (a1,a2,a3,a4,sum)
		try:
			cursor.execute(action)
		except Exception,e:
			print e
		cursor.close()
		save.close()
	except:
		out=str("请确认输入的是数字而不是其他字符！！！")
		print "请确认输入的是数字而不是其他字符！！！"
		tkMessageBox.showinfo(title="警告",message=out)
def analysis():
	try:
		save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
			#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
	except Exception,e:
		print e
		sys.exit()
	
	cursor=save.cursor()
		
	action="select id,profit from n_stock"
	try:
		cursor.execute(action)
	except Exception,e:
		print e
	num=cursor.fetchall()
	cursor.close()
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
	#print x,y

	plt.plot(x,y)
	plt.show()
Button(root,text='submit',command=click).pack()
Button(root,text='submit(含手续费)',command=dex).pack()
Button(root,text='analysis',command=analysis).pack()

root.mainloop()