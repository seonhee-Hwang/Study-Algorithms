# 마인크래프트 문제
'''
좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. --> 2초 걸림
인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. --> 1초 걸림
'''
# 땅 고르기에 걸리는 최소 시간과 땅의 높이를 출력하시오
# 작업을 시작할 때는 B개의 블록이 있다
# 땅의 높이는 256을 초과할 수 없으며, 음수가 될 수 없다.

# 첫째줄에 N, M, B가 주어진다. (N이 세로 개수, M이 가로 개수, B가 블록의 개수)
# 둘째줄부터 N개의 줄에, M개의 정수로 땅의 높이가 주어진다. 땅은 0 ~ 256 사이의 자연수

# 땅을 고르는데 걸리는 시간과 땅의 높이를 출력, 답이 여러개라면, 그 중 땅의 높이가 가장 높은 것을 출력

'''
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

2 0
'''

'''
3 4 1
64 64 64 64
64 64 64 64
64 64 64 63

1 64
'''

N, M, B = map(int, input().split())

height = []
min_height = 256
max_height = 0

# 흠... 쌓는것 1초, 캐내는 것 2초
# 쌓는 개수

for i in range(N):
    height.append(list(map(int, input().split())))
    min_height = min(min_height, min(height[-1]))
    max_height = max(max_height, max(height[-1]))

# print(min_height)
# print(max_height)

min_time = 1e9
result_height = 0
for target in range(min_height, max_height + 1):
    add_cnt = 0
    rm_cnt = 0
    for i in range(N):
        for j in range(M):
            if height[i][j] < target:
                add_cnt += target - height[i][j]
            elif height[i][j] > target:
                rm_cnt += height[i][j] - target
            else:
                pass
    
    if add_cnt > B + rm_cnt:
        continue
    else:
        tmp_time = add_cnt * 1 + rm_cnt * 2
        if min_time < tmp_time:
            continue
        else:
            min_time = tmp_time
            result_height = target

print(min_time, result_height)