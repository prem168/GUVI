x=int(input())
a=[]
y=list(map(int,input().split(" ")))
s=sum(y)
if(x>3):
    for i in range(0,x-1):
        p=s-y[i]-y[i-1]-y[i+1]
        a.append(p)
    print(max(a))
else:
    print(0)
