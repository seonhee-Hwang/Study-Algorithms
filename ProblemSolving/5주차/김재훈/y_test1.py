p, q = map(int, input().split())
r, s = map(int, input().split())
x, y = map(int, input().split())

# distance = [x - p, x - r, y - q, y - s]
distance = [x - p, r - x, y - q, s - y]
# abs_distance = map(abs, distance)

print(min(distance))