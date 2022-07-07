N , M, B = map(int, input().split())
sq = []
cnt_list = []
sum = 0
avg = 0
cnt = 0
#min_l, max_l = 0
for i in range(N):

    l = list(map(int, input().split()))
    for j in range(len(l)):
        sum += l[j]
    # sq.append(l)
    avg = sum/(len(l)*(i+1))
    for k in range(len(l)):
        if round(avg) == l[k]:
            continue
        else:
            if l[k] > round(avg):
                cnt += 2
            elif l[k] < round(avg):
                cnt += 1
            else:
                continue

print(cnt, round(avg))
# # print(cnt_list)
# # print(sq)