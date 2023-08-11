test_case = int(input())

for case in range(1, test_case + 1):
    d, l, n = map(int, input().split())
    damage = 0

    for i in range(0, n):
        damage += d * (1 + i * (l / 100))

    print(f'#{case} {int(damage)}')
