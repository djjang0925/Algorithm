import sys
input = sys.stdin.readline

from collections import deque


def bfs(s):
    q = deque(s)

    while q:
        y, x = q.popleft()

        if y == r - 1 or y == 0 or x == c - 1 or x == 0:
            if graph[y][x] == 'J':
                return res[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c:
                if graph[ny][nx] == '.' and res[ny][nx] == 0:
                    if graph[y][x] == 'J':
                        graph[ny][nx] = 'J'
                        res[ny][nx] = res[y][x] + 1

                    if graph[y][x] == 'F':
                        graph[ny][nx] = 'F'

                    q.append([ny, nx])

    return 'IMPOSSIBLE'


r, c = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(r)]
res = [[0] * c for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
root = []

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            root.append([i, j])
        
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            root.append([i, j])
            res[i][j] = 1

ans = bfs(root)

print(ans)