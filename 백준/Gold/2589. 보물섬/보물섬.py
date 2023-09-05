from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    global res
    q = deque([root])
    time = [[0] * m for _ in range(n)]
    time[root[0]][root[1]] = 1
    now = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'L' and time[ny][nx] == 0:
                    time[ny][nx], now = time[y][x] + 1, time[y][x] + 1
                    q.append([ny, nx])

    if now > res:
        res = now


n, m = map(int, input().rstrip().split())
graph = [list(input()) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            bfs([i, j])

print(res - 1)
