x=int(input())
a=list(map(int,input().split()))
f=1
for i in range(0,x):
    f=f*a[i]
for i in range(0,x-1):
    print(f//a[i],end=" ")
print(f//a[x-1])
