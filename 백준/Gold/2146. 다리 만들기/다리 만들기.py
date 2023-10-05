from collections import deque

import sys
input = sys.stdin.readline


def change(r):
    q = deque([r])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = -1
                    q.append([ny, nx])

                if graph[ny][nx] == 0:
                    root.append([y, x])


def bfs(r):
    q = deque([r])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])

                if graph[ny][nx] == 1:
                    temp.append(visited[y][x] - 1)
                    return


n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
temp = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            root = []
            graph[i][j] = -1
            change([i, j])

            for a, b in root:
                visited = [[0] * n for _ in range(n)]
                visited[a][b] = 1
                bfs([a, b])

print(min(temp))