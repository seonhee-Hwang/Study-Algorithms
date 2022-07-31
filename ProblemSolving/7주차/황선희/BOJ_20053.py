n = int(input())
for i in range(n):
    index = int(input())
    data = list(map(int, input().split()))
    data_max = max(data)
    data_min = min(data)
    print(data_min, data_max)