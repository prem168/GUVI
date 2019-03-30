a,b=input().split(" ")
a=int(a)
b=int(b)
m=list(map(int,input().split(" ")))
l=[]
while(b>0):
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    s=0
    for i in range(x-1,y):
       n=s^m[i]
       s=n
    l.append(s)
    b-=1
for i in range(0,len(l)):
    print(l[i])
