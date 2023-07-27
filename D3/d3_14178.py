test_case = int(input())

for case in range(1, test_case + 1):
    flower, sprayer = map(int, input().split())
    res = flower // (sprayer * 2 + 1)

    if flower % (sprayer * 2 + 1) == 0:
        print(f'#{case} {flower // (sprayer * 2 + 1)}')
    else:
        print(f'#{case} {flower // (sprayer * 2 + 1) + 1}')