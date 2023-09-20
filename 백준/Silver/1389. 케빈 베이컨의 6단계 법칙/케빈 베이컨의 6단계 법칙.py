import heapq

import sys
input = sys.stdin.readline


def dijkstra(start):
    heap = [(0, start)]
    kevin[start] = 0

    while heap:
        count, friend = heapq.heappop(heap)

        if count > kevin[friend]:
            continue

        for i in people[friend]:
            now = count + 1

            if now < kevin[i]:
                kevin[i] = now
                heapq.heappush(heap, (now, i))


n, m = map(int, input().rstrip().split())
people = {i: set() for i in range(1, n + 1)}
cnt = 21e8
res = 0

for i in range(m):
    a, b = map(int, input().rstrip().split())
    people[a].add(b)
    people[b].add(a)

for i in range(1, n + 1):
    kevin = [21e8] * (n + 1)
    dijkstra(i)

    if sum(kevin[1:]) < cnt:
        cnt = sum(kevin[1:])
        res = i

print(res)