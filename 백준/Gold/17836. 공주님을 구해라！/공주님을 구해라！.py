from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0] * m for _ in range(n)]
    visited_s = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque([root])

    while q:
        y, x, t, s = q.popleft()

        if y == n - 1 and x == m - 1:
            return t

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if s == 0:
                    if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        q.append([ny, nx, t + 1, s])
                    elif graph[ny][nx] == 2:
                        q.append([ny, nx, t + 1, 1])
                elif s == 1:
                    if visited_s[ny][nx] == 0:
                        visited_s[ny][nx] = 1
                        q.append([ny, nx, t + 1, s])

    return time + 1


n, m, time = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = bfs([0, 0, 0, 0])

if res <= time:
    print(res)
else:
    print('Fail')
