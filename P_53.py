x=str(input())
x=x.lower()
l=len(x)
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(x[i] in a):
		a.remove(x[i])
if(len(a)==0):
	print("yes")
else:
	print("no")
