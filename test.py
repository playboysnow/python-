# coding=utf-8
import sys,MySQLdb
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')
conn=MySQLdb.connect(host='rm-bp12a3q2p8q14i0yk.mysql.rds.aliyuncs.com',user='re5sh0bjj8',passwd='Mysqlweb20',db='re5sh0bjj8')
cur=conn.cursor()

cur.execute('insert into stock(b_price,s_price,num,rate,profit) values (5,5,1,1,1)')

cur.execute('select id,profit from stock')
num=cur.fetchall()
print num

cur.close()
#conn.commit()
conn.close()