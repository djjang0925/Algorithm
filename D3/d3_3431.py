test_case = int(input())

for case in range(1, test_case + 1):
    l, u, x = map(int, input().split())
    res = 0

    if u - x < 0:
        res = -1
    elif l - x > 0:
        res = l - x
    else:
        res = 0

    print(f'#{case} {res}')

