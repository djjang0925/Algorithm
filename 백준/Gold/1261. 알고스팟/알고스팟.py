import sys
input = sys.stdin.readline

import heapq


def dijkstra(st):
    heap = [st]

    while heap:
        wall, y, x = heapq.heappop(heap)

        if wall > res[y][x]:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                n_wall = wall + graph[ny][nx]

                if n_wall < res[ny][nx]:
                    res[ny][nx] = n_wall
                    heapq.heappush(heap, (n_wall, ny, nx))


m, n = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

res = [[21e8] * m for _ in range(n)]
res[0][0] = graph[0][0]

dijkstra((graph[0][0], 0, 0))

print(res[n - 1][m - 1])