input_brc = input()
stack = []

for i in range(len(input_brc)):
    if input_brc[i] in '({[':
        stack.append(input_brc[i])
    elif input_brc[i] in ')}]':
        if len(stack) != 0:
            if input_brc[i] == '(':
                if stack.pop() == ')':
                    print("True")
                else:
                    print("False")

            elif input_brc[i] == '{':
                if stack.pop() == '}':
                    print("True")
                else:
                    print("False")

            elif input_brc[i] == '[':
                if stack.pop() == ']':
                    print("True")
                else:
                    print("False")
        else:
            print("False")
    else:
        print("False")
