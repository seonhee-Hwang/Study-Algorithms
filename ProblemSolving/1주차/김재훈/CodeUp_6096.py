go_board = []

for i in range(19):
    go_board.append(list(map(int, input().split())))

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    for row in range(1, 20):
        for col in range(1, 20):
            if row == x and col == y:
                pass
            elif row == x or col == y:
                go_board[row-1][col-1] = 0 if go_board[row-1][col-1] == 1 else 1
                
for i in range(19):
    for j in range(19):
        print(go_board[i][j], end=' ')
    print()