a,b=input().split()
a=int(a)
b=int(b)
if(a>b):
    m=b
else:
    m=a
for i in range(1,m+1):
    if(a%i==0 and b%i==0):
        x=i
print(x)
