def dfs(s):
    stack = [s]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while stack:
        m = stack.pop()

        for i in range(4):
            y = m[0] + dy[i]
            x = m[1] + dx[i]

            if 0 <= y < n and 0 <= x < n:
                if graph[y][x] == '3':
                    return 1
                elif graph[y][x] == '0':
                    graph[y][x] = 1
                    stack.append([y, x])

    return 0


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '2':
                print(f'#{case} {dfs([i, j])}')
                flag = True
                break
        if flag is True:
            break
