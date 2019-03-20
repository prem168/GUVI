x=int(input())
a=list(map(int,input().split()))
a=a[::-1]
l=len(a)
for i in range(0,l-1):
    print(a[i],end="->")
print(a[l-1],end="")
