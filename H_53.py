x,y=input().split(" ")
x=str(x)
y=int(y)
l=len(x)
for i in range(0,l-y):
    print(x[i:i+y],end=" ")
print(x[i+1:i+y+1])
