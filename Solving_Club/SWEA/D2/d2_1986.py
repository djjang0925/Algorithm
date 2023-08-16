test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    res = 0

    for i in range(1, n + 1):
        if i % 2 == 1:
            res += i
        else:
            res -= i

    print(f'#{case} {res}')
