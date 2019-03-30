n=int(input())
x=list(map(int,input().split(" ")))
s=1
c=1
for i in range(0,len(x)-1):
    if(x[i]<x[i+1]):
        c=c+1
        s=s+c
    else:
        c=1
        s=s+c
if(x[i+1]<x[len(x)-1]):
    c=c+1
    s=s+c
else:
    s+=1
print(s-1)
