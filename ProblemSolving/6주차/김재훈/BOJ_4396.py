# 지뢰찾기

# 내가 할일 : 격자를 출력하기

# 입력
# 10보다 작은 양의 정수 n이 입력 (n x n 격자)
# 다음 n개의 줄은 지뢰의 위치를 표시
# .은 지뢰가 없는 지점, *은 지뢰가 있는 지점
# 그 다음 n개의 줄은 열린 칸을 표시
# .은 열리지 않은 칸, x는 이미 열린칸을 의미

# 출력
# 열린 칸에 숫자 표시하기 (주변 지뢰 개수)
# 지뢰가 터진 상태라면 모든 지뢰의 위치를 *로 표시할 것

n = int(input())

mine_board = [[]]
click_board = [[]]
result_board = [[0] * (n + 1) for i in range(n + 1) ]

# print(result_board)

for _ in range(n):
    tmp = list(input())
    tmp.insert(0, 0)
    mine_board.append(tmp)

for _ in range(n):
    tmp = list(input())
    tmp.insert(0, 0)
    click_board.append(tmp)

# print(mine_board)
# print("========")
# print(click_board)

def is_mine_clicked():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if click_board[i][j] == 'x' and mine_board[i][j] == '*':
                return True
    return False

def is_in_board(_i, _j):
    if 1 <= _i <= n and 1 <= _j <= n:
        return True
    else:
        return False

def calc_mine_cnt(_i, _j):
    cnt = 0
    x = [-1, -1, -1, 0, 0, +1, +1, +1] # 왼쪽 상단부터 오른쪽 하단까지
    y = [-1, 0, +1, -1, +1, -1, 0, +1] # 왼쪽 상단부터 오른쪽 하단까지

    for i in range(8):
        tmp_x = _i + x[i]
        tmp_y = _j + y[i]
        if is_in_board(tmp_x, tmp_y):
            if mine_board[tmp_x][tmp_y] == '*':
                cnt += 1
    return str(cnt)

    


if is_mine_clicked():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mine_board[i][j] == '*':
                result_board[i][j] = '*'

            elif click_board[i][j] == 'x' and mine_board[i][j] == '.':
                result_board[i][j] = calc_mine_cnt(i, j)
            
            else:
                result_board[i][j] = '.'

else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if click_board[i][j] == 'x':
                result_board[i][j] = calc_mine_cnt(i, j)
            else:
                result_board[i][j] = '.'

print(result_board)

result_board.pop(0)
for i in result_board:
    i.pop(0)
    print(''.join(i))

