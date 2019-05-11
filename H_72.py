x=list(input().split(" "))
l=len(x)
for i in range(0,l,2):
    x[i]=''.join(reversed(x[i]))
for i in range(0,l-2):
    print(x[i],end=" ")
print(x[l-1])
