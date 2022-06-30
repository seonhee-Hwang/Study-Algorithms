n = int(input())
tri_list = []
# a <= b <= c
for i in range(1, n+1):
    a = i
    for b in range(a, n-a+1):
        c = n - a - b
        if c < b:
            break
        if a+b > c:
            tri_list.append([a, b, c])
print(tri_list)
print(len(tri_list))