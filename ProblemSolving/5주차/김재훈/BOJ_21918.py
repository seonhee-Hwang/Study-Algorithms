# 전구 문제
# 입력되는 명령에 따라, 전구의 상태를 변경하고 최종 전구의 상태를 출력하는 문제

N, M = map(int, input().split())

bulbs = list(map(int, input().split()))
bulbs.insert(0, 0)
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulbs[b] = c

    elif a == 2:
        for i in range(b, c + 1):
            if bulbs[i] == 1:
                bulbs[i] = 0
            else:
                bulbs[i] = 1

    elif a == 3:
        for i in range(b, c + 1):
            bulbs[i] = 0
    
    elif a == 4:
        for i in range(b, c + 1):
            bulbs[i] = 1
    
    else:
        print("input error")

print(*bulbs[1:])
