a,b=input().split()
a=int(a)
b=int(b)
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(0,b):

    x.append(y[i])
    print(max(x))
