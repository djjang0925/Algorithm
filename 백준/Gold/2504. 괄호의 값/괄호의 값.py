import sys

input = sys.stdin.readline


def pop(x):
    global flag
    temp = 0

    while 1:
        n = stack.pop()

        if n.isdigit():
            temp += int(n)

        elif n == '(':
            if x == ']':
                flag = True
                return
            elif x == ')':
                if temp == 0:
                    temp += 2
                else:
                    temp *= 2
                break

        elif n == '[':
            if x == ')':
                flag = True
                return
            elif x == ']':
                if temp == 0:
                    temp += 3
                else:
                    temp *= 3
                break

        if not stack:
            flag = True
            break

    stack.append(str(temp))


test_string = list(input().rstrip())
stack = []
flag = False

for i in range(len(test_string)):
    if test_string[i] == '(' or test_string[i] == '[':
        stack.append(test_string[i])
    elif test_string[i] == ')' or test_string[i] == ']':
        if not stack:
            flag = True
            break
        else:
            pop(test_string[i])
    else:
        flag = True
        break

if flag is False:
    for i in range(len(stack)):
        if stack[i] == '(' or stack[i] == '[':
            flag = True
            break

if flag is True:
    print(0)
else:
    res = sum(list(map(int, stack)))
    print(res)
