#
# import re
# T = int(input())
# input_list =[[] for _ in range(T) ]
# # print(input_list)
# for i in range(T):
#     L = int(input())
#     for j in range(L):
#         input_list[i].append(re.findall(r'\d+', input()))
# print(input_list)
#
low_tmp = []
high_tmp = []
mid_tmp = []
T = int(input())
for i in range(T):
    L = int(input())
    for j in range(3):
        low_tmp.append(list(map(int, input().split('-'))))
        high_tmp.append(list(map(int, input().split('-'))))
        mid_tmp.append(list(map(int, input().split('-'))))

        print(low_tmp, high_tmp, mid_tmp)

