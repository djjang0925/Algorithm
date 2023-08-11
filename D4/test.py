def dfs(y, x):
    global flag

    if arr[y][x] == 2:
        flag = 1
        return

    for j in range(4):
        dy = y + directy[j]
        dx = x + directx[j]

        if dy < 0 or dx < 0 or dy > N - 1 or dx > N - 1:
            continue
        if visited[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        dfs(dy, dx)

        if flag == 1:
            return


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    flag = 0
    directy = [0, 0, -1, 1]
    directx = [1, -1, 0, 0]

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                visited[i][j] = 1
                dfs(i, j)
                break

    print(f'#{test_case} {flag}')
