n_list = [0 for i in range(30)]
nn_list =[]
for i in range(28):
    n = int(input())
    n_list[n-1] = 1

for j in range(30):
    if n_list[j] == 0:
        nn_list.append(j+1)


print(min(nn_list))
print(max(nn_list))








