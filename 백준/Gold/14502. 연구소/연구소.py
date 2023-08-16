import sys
input = sys.stdin.readline
from collections import deque
import copy


def bfs(r):
    q = deque(r)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                q.append([ny, nx])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    return cnt


def recursion(level):
    global graph, res
    backup = copy.deepcopy(graph)

    if level == 3:
        temp = bfs(root)

        if res < temp:
            res = temp

        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                recursion(level + 1)
                graph = copy.deepcopy(backup)


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

root = []
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            root.append([i, j])

recursion(0)

print(res)
