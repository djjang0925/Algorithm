from collections import deque

import sys
input = sys.stdin.readline


def is_melt():
    global cnt, time
    temp = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                temp += 1
            if graph[i][j] == -1:
                graph[i][j] = 0

    if temp > 0:
        cnt = temp
        time += 1
        return False
    else:
        return True


def change(root):
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if graph[ny][nx] == 0:
                graph[ny][nx] = -1
                q.append([ny, nx])


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
time = 0
cnt = 0

while not is_melt():
    check = [[0] * m for _ in range(n)]
    air = False

    for i in range(n):
        for j in range(m):
            if air is False and graph[i][j] == 0:
                graph[i][j] = -1
                change([i, j])
                air = True

            if graph[i][j] == 1:
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]

                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue

                    if graph[ni][nj] == -1:
                        graph[i][j] = 0
                        break

print(time)
print(cnt)