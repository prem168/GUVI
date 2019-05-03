w=list(map(int,input().split(" ")))
x=list(map(int,input().split(" ")))
y=list(map(int,input().split(" ")))
z=list(map(int,input().split(" ")))
if(w[1]==x[0] and x[1]==y[0] and y[1]==z[0] and z[1]==w[0]):
    print("yes")
else:
    print("no")
