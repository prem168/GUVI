n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
for i in range(0,n-1):
    if(x[n-2]==y[i] and x[n-1]==y[i+1]):
        c=n-2-i
        print(c)
        break
