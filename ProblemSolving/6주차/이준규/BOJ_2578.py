# 7.24
# 답은 3 나오지만 백준 제출시 틀림.
b_num_list = []
check_list = [[0 for _ in range(5)] for _ in range(5)]

for _ in range(5):
    b_num_list.append(list(map(int, input().split())))


# 빙고확인 check_bingo
def check_bingo(ls):
    cnt_row = 0
    cnt = 0
    # 1. cnt_row
    for i in range(5):
        for ii in range(5):
            if ls[i][ii] == 0:
                cnt_row += 1
            # print("cnt_row")
            # print(ls)
        if cnt_row == 5:
            # print("Cr")
            cnt += 1
    # 2. cnt_col
    cnt_col = 0
    for j in range(5):
        for jj in range(5):
            if ls[j][jj] == 0:
                cnt_col += 1
            # print("cnt_col")
            # print(ls)
        if cnt_col == 5:
            # print("Cc")
            cnt += 1
    # 3. cnt_lr_dg
    cnt_lr_dg = 0
    for k in range(5):
        if ls[k][k] == 0:
            cnt_lr_dg += 1
            # print("cnt_lr")
            # print(ls)
    if cnt_lr_dg == 5:
        # print("Clr")
        cnt += 1

    # 4. cnt_rl_dg
    cnt_rl_dg = 0
    for n in range(5):
        if ls[n][4 - n] == 0:
            cnt_rl_dg += 1
            # print("cnt_rl")
            # print(ls)
    if cnt_rl_dg == 5:
        # print("Crl")
        cnt += 1

    return cnt


cnt = 0

for x in range(5):
    a = list(map(int, input().split()))
    # num_list.append(a)
    for k in range(5):
        for y in range(5):
            for z in range(5):
                if b_num_list[y][z] == a[k]:
                    b_num_list[y][z] = 0
                    # print("yes")

    cnt_tot = check_bingo(b_num_list)
    cnt += cnt_tot
    # print(cnt_tot)
    if cnt >= 3:
        print(x + 1)
        break
