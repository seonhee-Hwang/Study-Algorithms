row, col = map(int, input().split())

board = [[0] * col for _ in range(row)]

# for i in board:
#     for j in i:
#         print(j, end=' ')
#     print()

N = int(input())

dx = [0, 1]
dy = [1, 0]

for i in range(N):
    l, d, x, y = map(int, input().split())
    # board[x - 1][y - 1] = 1
    for j in range(l):
        # print(x - 1 + dx[d]* j, y - 1 + dy[d] * j)
        board[x - 1 + dx[d] * j][y - 1 + dy[d] * j] = 1

for i in board:
    for j in i:
        print(j, end=' ')
    print()
        
    
    