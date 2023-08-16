def check(x):
    stack = []

    for i in range(int(n)):
        if not stack or x[i] != stack[-1]:
            stack.append(x[i])
        else:
            stack.pop()

    return stack


for case in range(1, 11):
    n, test_string = input().split()
    test_list = list(test_string)

    res = check(test_list)

    print(f'#{case}', ''.join(res))
