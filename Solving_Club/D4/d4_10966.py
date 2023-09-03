from collections import deque


def bfs(r):
    global res
    q = deque(r)

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if water[ny][nx] == 'W':
                    continue

                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])
                    res += graph[ny][nx]


for case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    water = [input() for _ in range(n)]
    graph = [[0] * m for _ in range(n)]
    root = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    res = 0

    for i in range(n):
        for j in range(m):
            if water[i][j] == 'W':
                root.append([i, j])

    bfs(root)

    print(f'#{case} {res}')
