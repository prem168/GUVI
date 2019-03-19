# PSV
x,y,z=input().split(" ")
x=int(x)
y=int(y)
z=int(z)
if(x>y):
	if(x>z):
		print(x)
	else:
		print(z)
else:
	if(y>z):
		print(y)
	else:
		print(z)
