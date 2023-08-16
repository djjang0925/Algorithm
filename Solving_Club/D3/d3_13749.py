def puzzle(y, x):
    cnt_y, cnt_x = 0, 0
    total = 0

    for i in range(x, n):
        if test_list[y][i] == 1:
            cnt_x += 1
        else:
            break

    for i in range(y, n):
        if test_list[i][x] == 1:
            cnt_y += 1
        else:
            break

    if cnt_y == k and y > 0:
        if test_list[y-1][x] == 0:
            total += 1
    elif cnt_y == k and y == 0:
        total += 1

    if cnt_x == k and x > 0:
        if test_list[y][x-1] == 0:
            total += 1
    elif cnt_x == k and x == 0:
        total += 1

    return total


test_case = int(input())

for case in range(1, test_case + 1):
    n, k = map(int, input().split())
    test_list = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            if test_list[i][j] == 1:
                res += puzzle(i, j)

    print(f'#{case} {res}')
