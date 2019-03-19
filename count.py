ch=int(input())
p=0
n=[]
x=list(map(int,input().split()))
c=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,ch):
	c[x[i]]+=1
for i in range(0,10):
	if(c[i]>1):
		n.append(i)
l=len(n)
if(l>0):
	for i in range(0,l-1):
		print(n[i],end=" ")
	print(n[l-1])
else:
	print("unique")
