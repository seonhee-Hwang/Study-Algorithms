# 윤년 문제
# 주어진 년도가 윤년이면 1, 아니면 0 출력
# 윤년의 정의 --> 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
# 2012년은 4의 배수이면서, 100의 배수가 아니므로 윤년
# 1900년은 4의 배수이지만, 100의 배수이므로 윤년 아님
# 2000년은 4의 배수이지면, 100의 배수이므로 아닐 것 같지만, 400의 배수라서 윤년

year = int(input())

result = 1
if year % 400 == 0:
    pass
elif year % 100 == 0:
    result = 0
elif year % 4 == 0:
    pass
else:
    result = 0

print(result)

# year = int(input())

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print('1')
# else:
#     print('0')