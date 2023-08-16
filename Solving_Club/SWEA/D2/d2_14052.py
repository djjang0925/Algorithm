from collections import deque


def bfs(r):
    q = deque([r])
    cnt = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == '0':
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])
                elif graph[ny][nx] == '2':
                    return graph[y][x]

    return 0


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    root = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '3':
                root = [i, j]
                graph[i][j] = 0
                break

    res = bfs(root)

    print(f'#{case} {res}')
