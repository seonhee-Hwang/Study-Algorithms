T = int(input())

for i in range(T):
    L = int(input())
    cnt = 0
    low_tmp = list(map(int, input().split('-')))
    high_tmp = list(map(int, input().split('-')))
    mid_tmp = list(map(int, input().split('-')))

    ls = [low_tmp, high_tmp, mid_tmp]
    # print(ls)
    for m in range(len(ls)):
        l = ls[m]
        for i in range(len(l)):
            change = bin(l[i])[2:]
            l[i] = str(change).rjust(8, "0")
    # print(ls)
    for j in range(L):
        for k in range(8):
            if low_tmp[j][k] == high_tmp[j][k] == mid_tmp[j][k]:
                continue
            else:
                cnt += 1
    print(cnt)

