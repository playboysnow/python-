# coding=utf-8
import sys,MySQLdb
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')
conn=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock',port=3306)
cur=conn.cursor()
cur.execute('select id,profit from n_stock')
num=cur.fetchall()
print num
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


cur.close()
conn.close()
plt.plot(x,y)
plt.show()