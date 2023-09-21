import heapq

import sys
input = sys.stdin.readline


def dijkstra(start):
    heap = [(0, start)]
    res[start] = 0

    while heap:
        price, stop = heapq.heappop(heap)

        if price > res[stop]:
            continue

        for i in cities[stop]:
            n_price = price + i[0]

            if n_price < res[i[1]]:
                res[i[1]] = n_price
                heapq.heappush(heap, (n_price, i[1]))


n, m = [int(input()) for _ in range(2)]
cities = {i: [] for i in range(1, n + 1)}

for i in range(m):
    s, e, c = map(int, input().rstrip().split())
    cities[s].append((c, e))

st, ed = map(int, input().rstrip().split())
res = {i: 21e8 for i in range(1, n + 1)}
dijkstra(st)

print(res[ed])