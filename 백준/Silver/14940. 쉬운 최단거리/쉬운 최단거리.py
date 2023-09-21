from collections import deque

import sys
input = sys.stdin.readline


def bfs(root):
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    res[ny][nx] = 1 + res[y][x]
                    q.append([ny, nx])


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = [[0] * m for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
flag = False

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs([i, j])
            flag = True
            break

    if flag is True:
        break

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res[i][j] = -1

for i in res:
    print(*i)