import sys
input = sys.stdin.readline

from collections import deque


def bfs(r):
    q = deque(r)

    while q:
        y, x = q.popleft()

        if y == 0 or y == h - 1 or x == 0 or x == w - 1:
            if graph[y][x] == '@':
                print(temp[y][x])
                return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if temp[ny][nx] == 0 and graph[ny][nx] == '.':
                    if graph[y][x] == '*':
                        graph[ny][nx] = '*'

                    if graph[y][x] == '@':
                        graph[ny][nx] = '@'
                        temp[ny][nx] = temp[y][x] + 1

                    q.append([ny, nx])

    print('IMPOSSIBLE')


for i in range(int(input())):
    w, h = map(int, input().rstrip().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    temp = [[0] * w for _ in range(h)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    root = []

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                root.append([i, j])

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                temp[i][j] = 1
                root.append([i, j])

    bfs(root)