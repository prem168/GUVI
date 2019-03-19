ch = int(input())
n = []
x = list(map(int, input().split()))
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, ch):
    c[x[i]] += 1
for i in range(0, 10):
    if (c[i] >0):
        n.append(i)
for i in range(0,len(n)):
    if(c[n[i]]<2):
        print(n[i])
