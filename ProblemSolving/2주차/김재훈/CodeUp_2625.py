N = int(input())

# 합이 N이 되는 자연수 3개 찾는 문제
# N - 2, 1, 1
# N - 3, 1, 2

result = set()
for i in range(N - 2, 1, -1): # 7부터 2까지 동작
    for j in range(N - i - 1, 0, -1):
        tmp = [i, j, N - i - j]
        tmp.sort()
        if tmp[2] < tmp[0] + tmp[1]:
            # print(''.join(map(str, tmp)))
            result.add(''.join(map(str, tmp)))

print(len(result))