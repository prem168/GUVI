n,m=input().split(" ")
n=int(n)
m=int(m)
x=list(map(int,input().split()))
s=0
for i in range(m):
	s+=x[i]	
print(s)
