import heapq

import sys
input = sys.stdin.readline


def dijkstra(s):
    heap = [(0, s)]
    h_to_p[s] = 0

    while heap:
        time, way = heapq.heappop(heap)

        if time > h_to_p[way]:
            continue

        for i in roads[way]:
            n_time = time + i[0]

            if n_time < h_to_p[i[1]]:
                h_to_p[i[1]] = n_time
                heapq.heappush(heap, (n_time, i[1]))


n, m, x = map(int, input().rstrip().split())
roads = {i: [] for i in range(1, n + 1)}
maximum = 0

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    roads[a].append((c, b))

h_to_p = {i: 21e8 for i in range(1, n + 1)}
dijkstra(x)
p_to_h = h_to_p.copy()

for i in range(1, n + 1):
    h_to_p = {i: 21e8 for i in range(1, n + 1)}
    dijkstra(i)

    if h_to_p[x] + p_to_h[i] > maximum:
        maximum = h_to_p[x] + p_to_h[i]

print(maximum)