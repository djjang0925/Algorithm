from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    q = deque([root])
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        z, y, x = q.popleft()
        if y == n - 1 and x == m - 1:
            return visited[z][y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and z == 0:
                    visited[1][ny][nx] = visited[z][y][x] + 1
                    q.append([1, ny, nx])
                else:
                    if graph[ny][nx] == 0 and visited[z][ny][nx] == 0:
                        visited[z][ny][nx] = visited[z][y][x] + 1
                        q.append([z, ny, nx])

    return -1


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

res = bfs([0, 0, 0])

print(res)
