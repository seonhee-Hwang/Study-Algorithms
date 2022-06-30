num_Steps = int(input())
dp = []
Steps = []
for i in range(num_Steps):
    Steps.append(int(input()))
print(Steps)

# 마지막 필수 마지막전 : 마지막 -1 or 마지막 -2
for j in range(num_Steps):
    if j == 0:
        # 첫번째 계단 밟은경우의 최댓값 = 첫번째 계단
        check_1 = Steps[0]
        dp.append(check_1)

    elif j == 1:
        # 두번째 계단 밟은경우의 최댓값 = max(첫번째 게단까지 최댓값 + 두번째 계단, 두번째계단)
        check_2 = max(dp[0]+Steps[1],Steps[1])
        dp.append(check_2)
    elif j == 2:
        # 세번째 계단 밟은경우의 최댓값 = max(첫번째 계단까지 최댓값 + 세번째 계단, 두번째계단 + 세번째 계단)
        check_3 = max(dp[0]+Steps[2], Steps[1]+Steps[2])
        dp.append(check_3)

    else:
        # max ( 마지막 계단 + 전전계단까지의 최댓값, 마지막 계단 + 전계단 + 전전전계단까지의 최댓값)
        #  dp[j-3]  3칸전의 dp로 가면 3칸연속인경우 방지
        check_bigger = max(Steps[j] + dp[j-2], Steps[j] + Steps[j-1] + dp[j-3])
        dp.append(check_bigger)
print(dp)
print(dp[-1])