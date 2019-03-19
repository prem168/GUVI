ch = int(input())
def isp(n):
    c=0
    i=2
    m=n/2
    while(i<=m):
        if(n%i==0):
            c+=1
        i+=1
    if(c>0):
        print("no")
    else:
        print("yes")
isp(ch)
