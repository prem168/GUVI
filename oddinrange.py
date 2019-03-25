a,b=input().split(" ")
a=int(a)
b=int(b)
if(a%2==0):
    m=a+1
else:
    m=a+2
for i in range(m,b,2):
    if(b-i==1 or b-i==2):
        print(i)
        break
    print(i,end=" ")
