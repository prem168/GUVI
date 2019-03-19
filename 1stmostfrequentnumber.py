ch = int(input())
p = 0
m = 0
n = []
x = list(map(int, input().split()))
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, ch):
    c[x[i]] += 1
    if (c[x[i]] > 1):
        m = 1
        print(x[i])
        break
if (m == 0):
    print("unique")
