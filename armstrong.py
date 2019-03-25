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
x=int(input())
print(ia(x))
