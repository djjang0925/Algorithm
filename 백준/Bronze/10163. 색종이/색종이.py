from collections import deque
import sys
input = sys.stdin.readline


def bfs(root, goal, paint):
    q = deque([root])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if root[0] <= ny < goal[0] and root[1] <= nx < goal[1]:
                if graph[ny][nx] != paint:
                    graph[ny][nx] = paint
                    q.append([ny, nx])


n = int(input())
graph = [[0] * 1001 for _ in range(1001)]

for i in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    bfs([a, b], [a + c, b + d], i + 1)

for i in range(1, n + 1):
    temp = 0

    for j in range(1001):
        for k in range(1001):
            if graph[j][k] == i:
                temp += 1

    print(temp)
