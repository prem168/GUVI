c=input()
c=c.split(" ")
l=len(c)
for i in range(0,l-1):
    print(c[i][::-1],end=" ")
print(c[l-1][::-1])
