# 최소, 최대 2

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(min(numbers), max(numbers))