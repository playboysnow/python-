import math,time
import datetime
def getnum(num):
	list=[]
	for i in range (1,num):
		if (num % i) ==0:
			list.append(i)
			#print i
	a=sum(list)
	#print a 
	return a

def calsum():
	print datetime.datetime.now()
	b=[]
	for i in range (2,10001):
		m=getnum(i)
		for j in range (2,10001):
			n=getnum(j)
			if i!=j and m==n:
				#while i!=j:
				b.append(i)
	y=list(set(b))			
	#print y
	total=sum(y)
	print total
	print datetime.datetime.now()
	return total
if __name__=="__main__":
	calsum()
'''
b=[]

	for j in range (1,300):
		n=getnum(j)
		if m==n:
			b.append(i)
				
print b
total=sum(b)
print total

b=[]
for i in range (2,10001):
	m=getnum(i)
	b.append(m)
print sum(b)
'''