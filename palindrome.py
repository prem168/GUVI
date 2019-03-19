ch = int(input())
x=ch
sum=0

while(ch>0):
    n=ch%10
    sum=sum*10+n
    ch=int(ch/10)
if(sum==x):
    print("yes")
else:
    print("no")
