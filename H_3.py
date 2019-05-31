x=int(input())
a=list(map(int,input().split()))
n=[]
c=0
for i in range(len(a)):
    if(i==a[i]):
        n.append(a[i])
        c=1
if(c==1):
    for i in range(len(n)-1):
        print(n[i],end=" ")
    print(n[-1])
else:
    print(-1)
