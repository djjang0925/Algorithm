def erase(y, x, m):
    while y < n:
        if table[y][x] == m:
            table[y][x] = 0
            y += 1
        else:
            table[y][x] = 0
            break


def move(y, x, m):
    table[y][x] = 0

    if m == 2:
        for i in range(y - 1, -1, -1):
            if table[i][x] == 0:
                continue

            if table[i][x] != m:
                table[i + 1][x] = m
                break
    elif m == 1:
        for i in range(y + 1, n):
            if table[i][x] == 0:
                continue

            if table[i][x] != m:
                table[i - 1][x] = m
                break


for case in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            if table[i][j] != 0:
                move(i, j, table[i][j])

    for i in range(n):
        for j in range(n):
            if table[i][j] != 0:
                res += 1
                erase(i, j, table[i][j])

    print(f'#{case} {res}')
