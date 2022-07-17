# 8진수 2진수 문제
# 입력으로 8진수가 주어지면, 2진수로 변환하는 문제

# 8진수 숫자가 주어짐, 333,334 길이를 넘지 않음

# oct_num = input()
# number = 0
# for i in range(len(oct_num)):
#     number += int(oct_num[i]) * (8 ** (len(oct_num) - i - 1))

number = int(input(), 8)

print(format(number, 'b'))