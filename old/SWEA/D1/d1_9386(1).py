test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    numbers = list(input().split('0'))
    res = 0

    for num in numbers:
        if len(num) > res:
            res = len(num)

    print(f'#{case} {res}')
