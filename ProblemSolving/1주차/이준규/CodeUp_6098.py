d = []
for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    d[i] = list(map(int, input().split()))
# print(len(d))
# print(len(d[0]))
x, y = 1, 1
run = 1
while run > 0:
    if d[x][y + 1] == 0:
        d[x][y] = 9
        y += 1

    elif d[x + 1][y] == 0:
        d[x][y] = 9
        x += 1

    elif d[x][y + 1] == 2:
        d[x][y] = 9
        d[x][y + 1] = 9
        break

    elif d[x + 1][y] == 2:
        d[x][y] = 9
        d[x + 1][y] = 9
        break
    else:
        d[x][y] = 9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
