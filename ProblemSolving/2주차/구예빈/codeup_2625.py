n = int(input())

triangle_array = []
for a in range(n,0,-1):
    if n-a > a:
        for b in range(n-a,0,-1):
            c = n-a-b
            if c != 0 and a >= b and a >= c:
                triangle_array.append([a,b,c])

triangle_array = set([tuple(sorted(item)) for item in triangle_array])
print(len(triangle_array))