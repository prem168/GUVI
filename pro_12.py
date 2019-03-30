x,y=input().split(" ")
x=int(x)
y=int(y)
m=list(map(int,input().split(" ")))
n=[]
for i in range(0,y):
    sum=0
    u,v=input().split(" ")
    u=int(u)
    v=int(v)
    for j in range(u-1,v):
        sum+=m[j]
    n.append(sum)
for i in range(0,len(n)):
    print(n[i])
