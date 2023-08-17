from collections import deque
import sys


def bfs(r):
    q = deque([r])
    dy = [-1, 1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, -1, 1, 1, -1, 1, -1]

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if island[ny][nx] == 1:
                    island[ny][nx] = 0
                    q.append([ny, nx])


while 1:
    w, h = map(int, input().rstrip().split())

    if w == 0 and h == 0:
        break

    island = [list(map(int, input().rstrip().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                island[i][j] = 0
                cnt += 1
                bfs([i, j])

    print(cnt)
