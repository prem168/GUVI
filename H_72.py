x=list(input().split(" "))
l=len(x)
for i in range(0,l,2):
    x[i]=''.join(reversed(x[i]))
if(l!=2):
    for i in range(0,l-2):
        print(x[i],end=" ")
else:
    print(x[0],end=" ")
print(x[l-1])
