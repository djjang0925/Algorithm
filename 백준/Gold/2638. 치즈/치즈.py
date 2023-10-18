from collections import deque

import sys
input = sys.stdin.readline


def is_melt(cheese):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return True

    return False


def change(root):
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if check[ny][nx] == 0:
                if graph[ny][nx] == 0:
                    check[ny][nx] = 1
                    q.append([ny, nx])
                else:
                    graph[ny][nx] += 1


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
time = 0

while is_melt(graph):
    time += 1
    check = [[0] * m for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                check[i][j] = 1
                change([i, j])
                flag = True
                break
        if flag is True:
            break

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0

            if graph[i][j] == 2:
                graph[i][j] = 1

print(time)