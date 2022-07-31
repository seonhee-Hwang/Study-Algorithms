#7.31
std_list = [i for i in range(1,31)]
for i in range(28):
  sb = int(input())
  if sb in std_list:
    std_list.remove(sb)
for i in range(2):
  print(std_list)