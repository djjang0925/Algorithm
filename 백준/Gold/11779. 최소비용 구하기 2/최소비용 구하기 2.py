import heapq

import sys
input = sys.stdin.readline


def dijkstra(s):
    heap = [(0, s)]
    fees[s] = 0

    while heap:
        fee, stop = heapq.heappop(heap)

        if fee > fees[stop]:
            continue

        for i in cities[stop]:
            n_fee = fee + i[0]

            if n_fee < fees[i[1]]:
                fees[i[1]] = n_fee
                routes[i[1]] = stop
                heapq.heappush(heap, (n_fee, i[1]))


n, m = [int(input()) for _ in range(2)]
cities = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    cities[a].append((c, b))

st, ed = map(int, input().rstrip().split())
fees = {i: 21e8 for i in range(1, n + 1)}
routes = {i: i for i in range(1, n + 1)}

dijkstra(st)

print(fees[ed])

res = []
while ed != st:
    res.append(ed)
    ed = routes[ed]
else:
    res.append(st)

print(len(res))
print(*res[::-1])