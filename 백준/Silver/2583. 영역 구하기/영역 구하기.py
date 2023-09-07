from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    q = deque([root])
    temp = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 2
                    q.append([ny, nx])
                    temp += 1

    res.append(temp)


m, n, k = map(int, input().rstrip().split())
point = [list(map(int, input().rstrip().split())) for _ in range(k)]
graph = [[1] * n for _ in range(m)]
cnt = 0
res = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


for square in point:
    sx, sy, ex, ey = square

    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 2
            cnt += 1
            bfs([i, j])

res.sort()

print(cnt)
print(*res)
