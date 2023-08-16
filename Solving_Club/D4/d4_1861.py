def dfs(r):
    stack = [r]
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    while stack:
        s = stack.pop()
        y = s[0]
        x = s[1]

        if visited[y][x] == 0:
            cnt += 1
            visited[y][x] = 1
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 <= ny < n) and (0 <= nx < n) and (test_list[ny][nx] == test_list[y][x] + 1):
                    stack.append([ny, nx])

    return [test_list[r[0]][r[1]], cnt]


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = [list(map(int, input().split())) for _ in range(n)]
    root = 2e128
    res = 0

    for i in range(n):
        for j in range(n):
            dfs_r = dfs([i, j])

            if dfs_r[1] > res:
                res = dfs_r[1]
                root = dfs_r[0]
            elif dfs_r[1] == res:
                if root > dfs_r[0]:
                    root = dfs_r[0]

    print(f'#{case} {root} {res}')
