n = int(input())
trap_list = [list(input()) for _ in range(n)]
check_list = [list(input()) for _ in range(n)]
res_list = [['.']*n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    for y in range(n):
        if trap_list[x][y] == '.' and check_list[x][y] == 'x':
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if trap_list[nx][ny] == '*':
                    cnt += 1

            res_list[x][y] = cnt

        if trap_list[x][y] == '*' and check_list[x][y] == 'x':
            for a in range(n):
                for b in range(n):
                    if trap_list[a][b] == '*':
                        res_list[a][b] = '*'

for l in range(n):
    for m in range(n):
        print(res_list[l][m], end='')
    print()