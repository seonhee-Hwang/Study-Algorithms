bingo_line = [0] * 12 # 가로 5, 세로 5, 대각 2
bingo_board = [[],
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0]]

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

find_bingo()
print(bingo_line)