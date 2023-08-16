def recursion(level):
    global res, path
    if path >= res:
        return

    if level == n:
        if path < res:
            res = path
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        path += test_list[level][i]
        visited[i] = 1
        recursion(level + 1)
        path -= test_list[level][i]
        visited[i] = 0


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    path = 0
    res = 21e8
    recursion(0)

    print(f'#{case} {res}')
