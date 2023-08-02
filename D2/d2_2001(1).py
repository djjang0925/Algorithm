def flapper(y, x):
    dead = 0

    for i in range(y, y + m):
        for j in range(x, x + m):
            dead += fly_list[i][j]

    return dead


test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(n)]
    access = n - m + 1
    max_kill = 0

    for i in range(access):
        for j in range(access):
            kill = flapper(i, j)

            if kill > max_kill:
                max_kill = kill

    print(f'#{case} {max_kill}')