# 과제 안내신분..?
# 한 줄에 숫자 하나씩, 제출한 학생의 번호가 입력됨 (28명)
# 제출하지 않은 학생의 번호를 한 줄에 하나 씩, 2개 입력 

not_report = set(range(1, 31))
# print(not_report)
for _ in range(28):
    not_report.remove(int(input()))

print(min(list(not_report)))
print(max(list(not_report)))
