x,y=input().split()
x=int(x)
y=int(y)
n=[]
m=list(map(int,input().split()))
for i in range(0,y):
    u,v=input().split(" ")
    u=int(u)
    v=int(v)
    n.append(sum(m[u-1:v]))
for i in range(0,len(n)):
    print(n[i])
