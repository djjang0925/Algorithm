from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    global max_width

    width = 1
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    width += 1
                    q.append([ny, nx])

    max_width = max(width, max_width)


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
max_width = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt += 1
            bfs([i, j])

print(cnt)
print(max_width)
