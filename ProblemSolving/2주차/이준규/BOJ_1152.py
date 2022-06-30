words = input().split()
# print(words)
print(len(words))

# #############
# # 시간초과 뜸 #
# #############
# stc = input()
# collect = []
# word = []
# cnt = 0
# w_f = 0
# w_l = 0
# temp =''
# for i in range(len(stc)):
#     collect.append(stc[i])
# # 첫번째, 마지막 공백 아닌경우 : 단어갯수 = 띄어쓰기 갯수 + 1
# if collect[0] != ' ' and collect[-1] != ' ':
#     for m in range(len(collect)):
#         if collect[m] == ' ':
#             cnt += 1
#     print(cnt+1)
# # 첫번째 or 마지막 공백인경우 공백 나올때마다 슬라이싱.
# else:
#     for j in range(len(collect)):
#         w_f = 0
#         w_l = j
#         if collect[j] == ' ':
#             for k in range(w_f,w_l+1):
#                 temp += collect[k]
#             word.append(k)
#             w_f = j+1
#             w_l = j+1
#     print(len(word))
#
