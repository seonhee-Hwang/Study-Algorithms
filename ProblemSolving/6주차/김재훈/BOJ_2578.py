# 빙고

# 5 X 5 빙고판
# 3줄 이상 지워지면 빙고
# 사회자가 몇 번째 수를 부른 후 빙고가 되는지 출력

# 입력
# 빙고 --> 5줄 동안, 5개의 숫자가 주어짐 (25개)
# 이 후, 5줄 동안, 5개의 숫자가 주어짐 (25개)

# 출력
# 몇 번째 숫자를 부르면 빙고가 되는지 파악

bingo_board = [[]]
bingo_line = [0] * 12 # 가로 5, 세로 5, 대각 2

for i in range(1, 6):
    tmp = list(map(int, input().split()))
    tmp.insert(0, 0)
    bingo_board.append(tmp)

bingo_input = [0] * 26
for i in range(5):
    bingo_input[i * 5 + 1 : i * 5 + 6] = list(map(int, input().split()))

def search(_n):
    for i in range(1, 6):
        for j in range(1, 6):
            if bingo_board[i][j] == _n:
                bingo_board[i][j] = 0
                return

def find_bingo_line_in_row():
    for i in range(1, 6):
        if bingo_line[i - 1] == 1:
            continue
        if sum(bingo_board[i][1:6]) == 0:
            bingo_line[i - 1] = 1
            
def find_bingo_line_in_column():
    for i in range(1, 6):
        if bingo_line[i - 1 + 5] == 1:
            continue
        sum = 0
        for j in range(1, 6):
            sum += bingo_board[j][i]
        if sum == 0:
            bingo_line[i - 1 + 5] = 1

def find_bingo_line_in_cross():
    if bingo_line[10] == 0:
        sum = 0
        for i in range(1, 6):
            sum += bingo_board[i][i]
        if sum == 0:
            bingo_line[10] = 1
    
    if bingo_line[11] == 0:
        sum = 0
        for i in range(1, 6):
            sum += bingo_board[i][6 - i]
        if sum == 0:
            bingo_line[11] = 1

def find_bingo():
    find_bingo_line_in_row()
    find_bingo_line_in_column()
    find_bingo_line_in_cross()
    return sum(bingo_line)

# print(bingo_board)
# print(bingo_input)
# print(bingo_line)

def print_bingo_board():
    for i in range(1, 6):
        print(*[bingo_board[i][1:6]])

for i in range(1, 26):
    if i <= 12:
        search(bingo_input[i])
    else:
        search(bingo_input[i])
        if find_bingo() >= 3:
            print(i)
            break

