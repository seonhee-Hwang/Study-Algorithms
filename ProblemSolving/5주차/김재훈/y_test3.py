lst = input()

stack = []
result = True
for i in lst:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    elif i == ')' or i == '}' or i == ']':
        if not stack:
            result = False
            break
        tmp = stack.pop() + i # '()' '{}' '[]'
        if tmp == '()' or tmp == '{}' or tmp == '[]':
            continue
        else:
            result = False
            break

if stack:
    result = False

print(result)