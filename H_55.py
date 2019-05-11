n,m=input().split(" ")
n=int(n)
m=int(m)
x=list(map(int,input().split()))
c=[]
c.extend(x[m:])
for i in range(0,m):
    c.append(x[i])
for i in range(0,n-1):
    print(c[i],end=" ")
print(c[n-1])
