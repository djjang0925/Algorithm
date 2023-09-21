import heapq

import sys
input = sys.stdin.readline


def dijkstra(start):
    heap = [(0, start)]
    routes[start] = 0

    while heap:
        price, stop = heapq.heappop(heap)

        if price > routes[stop]:
            continue

        for i in graph[stop]:
            n_price = price + i[0]

            if n_price < routes[i[1]]:
                routes[i[1]] = n_price
                heapq.heappush(heap, (n_price, i[1]))


v, e = map(int, input().rstrip().split())
st = int(input())
graph = {i: [] for i in range(1, v + 1)}
routes = {i: 21e8 for i in range(1, v + 1)}

for i in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))

dijkstra(st)

for i in routes:
    if routes[i] == 21e8:
        print('INF')
    else:
        print(routes[i])