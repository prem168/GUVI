a,b=input().split(" ")
a=int(a)
b=int(b)
k=0
x=list(map(int,input().split(" ")))
for i in range(0,a):
    for j in range(i+1,a):
        if(x[i]+x[j]==b):
            k=1
            print("yes")
            break
if(k==0):
    print("no")
