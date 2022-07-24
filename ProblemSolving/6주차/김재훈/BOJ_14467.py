# 소가 길을 건너간 이유 1

# 입력
# 1 ~ 10, 0 or 1
# 소의 번호, 길을 건너기 전, 후 상태가 출력

# 출력
# 전체 소가 길을 건넌 최소 횟수를 출력 
# (관측되지 않은 경우도 있을 수 있으므로 관측된 것의 합을 계산)

N = int(input())

cows = {}
cnts = 0
for _ in range(N):
    cow_id, position = map(int, input().split())
    if cow_id in cows:
        if cows[cow_id] == position:
            pass
        else:
            cnts += 1
            cows[cow_id] = position
    else:
        cows[cow_id] = position

print(cnts)
