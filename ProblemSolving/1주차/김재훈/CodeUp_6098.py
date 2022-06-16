# import time

board = []
for _ in range(10):
    board.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]
x, y = [1, 1]
# print(x, y)

while True:
    # time.sleep(1)
    if board[x][y] == 2:
        board[x][y] = 9
        break
    board[x][y] = 9
    # print(x, y)
    # print(x + dx[0], y + dy[0])
    # print(x + dx[1], y + dy[1])
    if board[x + dx[0]][y + dy[0]] != 1:
        x = x + dx[0]
        y = y + dy[0]
    elif board[x + dx[1]][y + dy[1]] != 1:
        x = x + dx[1]
        y = y + dy[1]
    else:
        break
    # print(x, y)
    
for i in board:
    for j in i:
        print(j, end= ' ')
    print()