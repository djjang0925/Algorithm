def permutation(level, battery, root):
    global res

    if level == n - 2:
        if battery + golf[root][0] < res:
            res = battery + golf[root][0]
        return

    for i in range(1, n):
        if path[i] == 1:
            continue

        path[i] = 1
        permutation(level + 1, battery + golf[root][i], i)
        path[i] = 0


for case in range(1, int(input()) + 1):
    n = int(input())
    golf = [list(map(int, input().split())) for _ in range(n)]
    path = {i: 0 for i in range(1, n)}
    res = 21e8

    for i in range(1, n):
        path[i] = 1
        permutation(0, golf[0][i], i)
        path[i] = 0

    print(f'#{case} {res}')
