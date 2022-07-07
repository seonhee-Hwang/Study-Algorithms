N = int(input())
Time_list =[ ]
dp = []
Sum = 0
Sum_list = []
# Total = 0
Time_list = list(map(int,input().split()))

Time_list.sort()
for j in range(1,len(Time_list)+1):
    for i in range(j):
        Sum += Time_list[i]
    Sum_list.append(Sum)
# print(Sum_list)
# print(max(Sum_list))
print(Sum_list[-1])