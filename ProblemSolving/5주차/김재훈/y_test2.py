t = int(input())

for _ in range(t):
    n = int(input())
    
    low = list(map(int, input().split('-')))
    high = list(map(int, input().split('-')))
    normal = list(map(int, input().split('-')))

    for i in range(n):
        low[i] = format(low[i], 'b')
        if len(low[i]) != 8:
            low[i] = '0' * (8 - len(low[i])) + low[i]
        
        high[i] = format(high[i], 'b')
        if len(high[i]) != 8:
            high[i] = '0' * (8 - len(high[i])) + high[i]
        
        normal[i] = format(normal[i], 'b')
        if len(normal[i]) != 8:
            normal[i] = '0' * (8 - len(normal[i])) + normal[i]

    cnt = 0

    for i in range(n):
        for j in range(8):
            if low[i][j] == high[i][j] == normal[i][j]:
                continue
            else:
                cnt += 1

    print(cnt)

