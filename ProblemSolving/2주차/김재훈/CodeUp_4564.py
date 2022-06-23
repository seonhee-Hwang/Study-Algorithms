# 1개 또는 2개를 오를 수 있음
# 이동할 수 있는 경우의 수는 1 1 2 or 2 1 1 or 1 2 1
# 연속된 3개를 올라서는 안됨 (2번 1개를 올랐으면, 2개를 올라야함)
# 마지막 계단은 무조건 올라야 함

# dp[n] = max(dp[n-2] + score[n], dp[n-3] + scores[n-1] + scores[n])
# 마지막에 두칸을 올라서 도착한 경우 or 두칸 한칸 올라서 도착한 경우로 나누어서 풀이

def calc_score(n):
    if dp[n] != 0:
        return dp[n]
    if n == 0:
        dp[n] = scores[0]
        return dp[n]
    elif n == 1:
        dp[n] = scores[0] + scores[1]
        return dp[n]
    elif n == 2:
        dp[n] = max(scores[0] + scores[2], scores[1] + scores[2])
        return dp[n]
    dp[n] = max(calc_score(n-3) + scores[n] + scores[n - 1], calc_score(n-2) + scores[n])
    return dp[n]

N = int(input())
dp = [0] * (N + 1)
scores = [0]
for _ in range(N):
    scores.append(int(input()))

print(calc_score(N))

