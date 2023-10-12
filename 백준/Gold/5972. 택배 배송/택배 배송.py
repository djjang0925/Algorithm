import heapq

import sys
input = sys.stdin.readline


def dijkstra(root):
    heap = [root]

    while heap:
        cost, cur = heapq.heappop(heap)

        if cost > costs[cur]:
            continue

        for i in graph[cur]:
            n_cost = cost + i[0]
            nxt = i[1]

            if n_cost < costs[nxt]:
                costs[nxt] = n_cost
                heapq.heappush(heap, (n_cost, nxt))


n, m = map(int, input().rstrip().split())
graph = {i: [] for i in range(1, n + 1)}
costs = {i: 21e8 for i in range(1, n + 1)}

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

dijkstra((0, 1))

print(costs[n])