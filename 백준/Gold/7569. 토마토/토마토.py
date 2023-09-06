from collections import deque
import sys
input = sys.stdin.readline


def bfs(r):
    q = deque(r)
    dz = [0, 0, 0, 0, -1, 1]
    dy = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]

    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = tomato[z][y][x] + 1
                    q.append([nz, ny, nx])


m, n, h = map(int, input().rstrip().split())
tomato = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]
root = []
res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                root.append([i, j, k])

bfs(root)
flag = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                flag = True
                break
            elif tomato[i][j][k] > res:
                res = tomato[i][j][k]
        if flag is True:
            break
    if flag is True:
        break
else:
    print(res - 1)
    