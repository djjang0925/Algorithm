def check(x):
    stack = []

    for i in range(len(x)):
        if not stack or x[i] != stack[-1]:
            stack.append(x[i])
        else:
            stack.pop()

    return stack


test_case = int(input())

for case in range(1, test_case + 1):
    test_string = list(input())

    res = check(test_string)

    print(f'#{case} {len(res)}')
