ch = int(input())
sum=0
while(ch>0):
    n=ch%10
    sum=sum*10+n
    ch=int(ch/10)
print(sum)
