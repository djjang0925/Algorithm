import sys
input = sys.stdin.readline

import heapq


def dijkstra(s):
    heap = [(0, s)]
    routes[s][s] = 0

    while heap:
        cur, stop = heapq.heappop(heap)

        if cur > routes[s][stop]:
            continue

        for i in graph[stop]:
            nxt = cur + i[0]

            if nxt < routes[s][i[1]]:
                routes[s][i[1]] = nxt
                heapq.heappush(heap, (nxt, i[1]))


n, m, r = map(int, input().rstrip().split())
items = [0] + list(map(int, input().rstrip().split()))
graph = {i: [] for i in range(1, n + 1)}
routes = {i: {j: 21e8 for j in range(1, n + 1)} for i in range(1, n + 1)}
res = 0

for i in range(r):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n + 1):
    dijkstra(i)

for i in range(1, n + 1):
    temp = 0

    for j in range(1, n + 1):
        if routes[i][j] <= m:
            temp += items[j]

    if temp > res:
        res = temp

print(res)