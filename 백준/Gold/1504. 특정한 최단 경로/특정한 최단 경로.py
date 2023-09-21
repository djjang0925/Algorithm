import heapq

import sys
input = sys.stdin.readline


def dijkstra(s):
    heap = [(0, s)]
    routes[s][s] = 0

    while heap:
        distance, stop = heapq.heappop(heap)

        if distance > routes[s][stop]:
            continue

        for i in graph[stop]:
            n_distance = distance + i[0]

            if n_distance < routes[s][i[1]]:
                routes[s][i[1]] = n_distance
                heapq.heappush(heap, (n_distance, i[1]))


n, e = map(int, input().rstrip().split())
graph = {i: [] for i in range(1, n + 1)}

for i in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

arr = [1] + list(map(int, input().rstrip().split()))
routes = {i: {j: 21e8 for j in range(1, n + 1)} for i in arr}

for i in arr:
    dijkstra(i)

res1 = routes[arr[0]][arr[1]] + routes[arr[1]][arr[2]] + routes[arr[2]][n]
res2 = routes[arr[0]][arr[2]] + routes[arr[2]][arr[1]] + routes[arr[1]][n]
res = min(res1, res2)

if res >= 21e8:
    print(-1)
else:
    print(res)