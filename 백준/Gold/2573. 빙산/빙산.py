from collections import deque

import sys
input = sys.stdin.readline


def find(y, x):
    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
           if graph[ny][nx] == 0:
               cnt += 1

    return cnt


def melt():
    water = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                water[i][j] = find(i, j)

    for i in range(n):
        for j in range(m):
            if graph[i][j] - water[i][j] <= 0:
                graph[i][j] = 0
            else:
                graph[i][j] -= water[i][j]


def bfs(root):
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] > 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0 ,0]
dx = [0, 0, -1, 1]
year = 0

while 1:
    year += 1
    melt()

    iceberg = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs([i, j])
                iceberg += 1

    if iceberg >= 2:
        print(year)
        break

    if iceberg == 0:
        print(0)
        break