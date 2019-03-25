a,b=input().split()
input()
a=int(a)
b=int(b)
x=list(map(int,input().split()))
y=list(map(int,input().split()))
i=0
while(i<b-1):

    x.append(y[i])
    print(max(x),end=" ")
    i+=1
x.append(y[i])
print(max(x))
