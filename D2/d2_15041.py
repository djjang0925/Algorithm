test_case = int(input())

for case in range(1, test_case + 1):
    test_list = list(input().split())
    calculator = ['+', '-', '*', '/', '%']
    stack = []

    print(f'#{case}', end=' ')

    for x in test_list:
        if x == '.':
            if not stack or len(stack) > 1:         # 스택에 숫자가 없거나 연산되지 않은 숫자가 여러개 남아 있을 경우
                print('error')
            else:
                print(stack.pop())
            break
        elif x.isdigit():
            stack.append(int(x))
        elif x in calculator:
            if len(stack) <= 1:
                print('error')
                break
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if x == '+':
                    stack.append(n1 + n2)
                elif x == '-':
                    stack.append(n1 - n2)
                elif x == '*':
                    stack.append(n1 * n2)
                elif x == '/':
                    stack.append(n1 // n2)
                elif x == '%':
                    stack.append(n1 % n2)
        else:
            print('error')
            break
