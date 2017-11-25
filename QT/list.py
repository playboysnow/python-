def b_list(l):
    count=len(l)
    for i in range(0,count):
        for j in range(0,count-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                print l
    return l
l=[4,2,6,1,3,4,10]
b_list(l)

def insert(l):
    count=len(l)
    for i in range(1,count):
        k=l[i]
        j=i-1
        while j>=0:
            if l[j]>k:
                l[j+1]=l[j]
                l[j]=k
            j-=1
    return l
w=[4,12,3,2,5,3,1,6,8,3]
#print insert(w)
import socket
socket.ntohl()