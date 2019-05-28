def rev(n):
    m=0
    while(n>0):
        p=n%10
        n=n//10
        m=m*10+p
    return m
x=int(input())
while(x%10==0):
    x=x/10
x=rev(x)
while(x%10==0):
    x=x/10
if(x==rev(x)):
    print("yes")
else:
    print("no")
