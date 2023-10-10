from collections import deque

import sys
input = sys.stdin.readline


def bfs(root):
    global ans
    q = deque([root])

    while q:
        y, x, c = q.popleft()

        if [y, x] == [n-1, m-1]:
            return visited[c][y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            
            if c < k:
                if graph[ny][nx] == '1'and visited[c + 1][ny][nx] == 0:
                    visited[c+1][ny][nx] = visited[c][y][x] + 1
                    q.append([ny, nx, c + 1])
            
            if graph[ny][nx] == '0' and visited[c][ny][nx] == 0:
                visited[c][ny][nx] = visited[c][y][x] + 1
                q.append([ny, nx, c])

    return -1


n, m, k = map(int, input().rstrip().split())
graph = list(input() for _ in range(n))
visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(bfs([0, 0, 0]))