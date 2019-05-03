x=int(input())
a=[]
y=list(map(int,input().split(" ")))
for i in range(0,x-2):
    m=0
    for j in range(i,x-1):
        if(y[j+1]>y[j]):
            m=m+1
        else:
            break
    a.append(m)
if(max(a)==0):
    print(0)
else:
    print(max(a)+1)
