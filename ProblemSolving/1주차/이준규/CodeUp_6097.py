h, w = map(int, input().split())
d = []
for i in range(h):
    d.append([])
    for j in range(w):
        d[i].append(0)

T = int(input())

for i in range(T):
    l, dd, x, y = map(int, input().split())
    if dd == 0:
        for j in range(l):
            d[x-1][y-1+j] = 1
    else:
        for j in range(l):
            d[x-1+j][y-1] = 1


for i in range(h):
    for j in range(w):
        print(d[i][j], end=' ')
    print()