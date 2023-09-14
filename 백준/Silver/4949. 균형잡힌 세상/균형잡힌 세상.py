while 1:
    string = list(input())
    stack = []

    if len(string) == 1 and string[0] == '.':
        break

    for i in string:
        if i == '(' or i == '[':
            stack.append(i)

        if i == ']':
            if not stack or stack[-1] == '(':
                print('no')
                break
            else:
                stack.pop()

        if i == ')':
            if not stack or stack[-1] == '[':
                print('no')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('no')
        else:
            print('yes')