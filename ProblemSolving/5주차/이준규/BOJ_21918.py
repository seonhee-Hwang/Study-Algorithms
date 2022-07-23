N, M = map(int, input().split())
# 1 : i 번째 전구상태 x
# 2 : l~r 번째 전구상태 변경 반대로
# 3 : l~ r OFF, 4 : l~r ON
s = list(map(int, input().split()))
# print(s)
for i in range(M):
    # a : 명령, b,c - > 1 : i,x / 2~4 : l~r
    # 0 : OFF, 1 : ON
    a, b, c = map(int, input().split())
    if a == 1:
        i, x = b, c
        s[i-1] = x
    elif a == 2:
        l, r = b, c
        for j in range(l-1, r):
            if s[j] == 1:
                s[j] = 0
            elif s[j] == 0:
                s[j] = 1
    elif a == 3:
        l, r = b, c
        for j in range(l-1, r):
            s[j] = 0
    elif a == 4:
        l, r = b, c
        for j in range(l-1, r):
            s[j] = 1

print(*s)
# for k in range(len(s)):
#     print(s[k], end=" ")
