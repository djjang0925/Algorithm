test_case = int(input())

for case in range(1, test_case + 1):
    h1, h2 = map(int, input().split())
    res = h1 + h2

    if res >= 24:
        res -= 24

    print(f'#{case} {res}')