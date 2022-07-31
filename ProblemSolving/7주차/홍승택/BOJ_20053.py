#7.31
T = int(input())
for i in range(T):
  N = int(input())
  list_ = list(map(int,input().split()))
  print(min(list_),max(list_))