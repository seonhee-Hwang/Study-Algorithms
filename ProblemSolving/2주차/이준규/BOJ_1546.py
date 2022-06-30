T = int(input())
score_list = list(map(int, input().split()))
new_score = score_list
max_score = max(score_list)
sum = 0
for i in range(len(score_list)):
    new_score[i] = score_list[i]/max_score * 100
    sum += new_score[i]

print(sum/T)