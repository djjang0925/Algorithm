def dfs(root, shape):
    stack = [root]
    if shape == '-':
        dy = [0, 0]
        dx = [1, -1]
    else:
        dy = [1, -1]
        dx = [0, 0]

    while stack:
        y, x = stack.pop()

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == shape:
                    graph[ny][nx] = 0
                    stack.append([ny, nx])


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            dfs([i, j], '-')
            cnt += 1
        elif graph[i][j] == '|':
            dfs([i, j], '|')
            cnt += 1

print(cnt)
