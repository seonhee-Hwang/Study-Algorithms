# 7.24
N = int(input())

cow_list = []
line_list = []
for i in range(N):
    n_cow, line = map(int,input().split())
    cow_list.append(n_cow)
    line_list.append(line)

max_cow_n = max(cow_list)
detect_cow = [[]for _ in range(max_cow_n)]

sum = 0
for j in range(N):
    detect_cow[cow_list[j]-1].append(line_list[j])
for k in range(len(detect_cow)):

    if len(detect_cow[k]) >= 2:
        # tmp = 0
        # cnt = 0
        tmp = -1
        cnt = -1

        for l in range(len(detect_cow[k])):
            if tmp != detect_cow[k][l]:
                tmp = detect_cow[k][l]
                # print(detect_cow[k][l])
                # print("check")
                cnt += 1
        sum += cnt

print(sum)
# print(detect_cow)