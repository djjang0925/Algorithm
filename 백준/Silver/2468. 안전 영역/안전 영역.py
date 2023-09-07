from collections import deque
import copy
import sys
input = sys.stdin.readline


def bfs(when, root):
    q = deque([root])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if when[ny][nx] != 0:
                    when[ny][nx] = 0
                    q.append([ny, nx])


n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = 0

for i in range(101):
    temp = copy.deepcopy(graph)
    cnt = 0

    for j in range(n):
        for k in range(n):
            if temp[j][k] <= i:
                temp[j][k] = 0

    for j in range(n):
        for k in range(n):
            if temp[j][k] != 0:
                bfs(temp, [j, k])
                cnt += 1

    res = max(res, cnt)

print(res)
