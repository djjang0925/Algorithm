import heapq

import sys
input = sys.stdin.readline


def dijkstra(st):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    heap = [st]

    while heap:
        cost, y, x = heapq.heappop(heap)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                n_cost = cost + graph[ny][nx]

                if n_cost < result[ny][nx]:
                    result[ny][nx] = n_cost
                    heapq.heappush(heap, (n_cost, ny, nx))


case = 1
while 1:
    n = int(input())

    if n == 0:
        break

    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    result = [[21e8] * n for _ in range(n)]
    result[0][0] = graph[0][0]

    dijkstra((graph[0][0], 0, 0))
    print(f'Problem {case}: {result[n - 1][n - 1]}')
    case += 1