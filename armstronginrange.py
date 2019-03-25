def ia(n):
    p=n
    sum=0
    while(n>0):
        m=n%10
        sum=sum+(m**3)
        n=n//10
    if(sum==p):
        return "yes"
    else:
        return "no"
x,b=input().split()
x=int(x)
b=int(b)
y=[]
for i in range(x+1,b):
    if(ia(i)=="yes"):
        y.append(i)
l=len(y)
i=0
while(i<l-1):
    print(y[i],end=" ")
    i+=1
print(y[l-1])
