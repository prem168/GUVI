x=int(input())
m=[]
n=[]
for i in range(0,x):
    m=list(map(int,input().split(" ")))
    n=n+m
n.sort()
for i in range(0,len(n)-1):
    print(n[i],end=" ")

print(n[i+1])
