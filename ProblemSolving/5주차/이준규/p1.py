p, q = map(int, input().split())
r, s = map(int, input().split())
x, y = map(int, input().split())

h_min, h_max, w_min, w_max = q, s, p, r
l = [ abs(h_min-y), abs(h_max-y), abs(w_min-x), abs(w_max-x) ]
print(min(l))
