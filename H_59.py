n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(0,n-1):
    print(x[i]+y[i],end=" ")
print(x[n-1]+y[n-1])
