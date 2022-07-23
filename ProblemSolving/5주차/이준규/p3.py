input_brc = input()
stack = []
res = True

for i in range(len(input_brc)):

    l = ['(', '[', '{']
    r = [')', ']', '}']

    if input_brc[i] in l:
        stack.append(input_brc[i])

    elif input_brc[i] in r:
        if r.index(input_brc[i]) == l.index(stack[-1]):
            stack.pop()
        else:
            break
res = False

if len(stack) == 0:
    res = True

print(res)
