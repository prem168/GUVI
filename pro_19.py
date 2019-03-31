x=int(input())
m=[]
n=[]
for i in range(0,x):
    m=list(map(int,input().split(" ")))
    n=n+m
n.sort()
l=len(n)
if(l>1):
    for i in range(0,l-1):
        print(n[i],end=" ")

print(n[l-1])
