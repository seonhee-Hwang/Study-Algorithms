std_n = [i for i in range(1, 31)]
std_sb = []
for i in range(28):
    sb = int(input())
    if sb in std_n:
        std_n.remove(sb)

for i in range(len(std_n)):
    print(std_n[i])
