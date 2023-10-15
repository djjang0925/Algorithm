import heapq

import sys
input = sys.stdin.readline


def dijkstra(root):
    heap = [root]
    times[root[1]] = 0

    while heap:
        time, cur = heapq.heappop(heap)

        for i in computers[cur]:
            n_time = time + i[0]

            if n_time < times[i[1]]:
                times[i[1]] = n_time
                heapq.heappush(heap, (n_time, i[1]))


for case in range(1, int(input()) + 1):
    n, d, c = map(int, input().rstrip().split())
    computers = {i: [] for i in range(1, n + 1)}
    times = {i: 21e8 for i in range(1, n + 1)}
    cnt = 0
    time = 0

    for i in range(d):
        a, b, s = map(int, input().rstrip().split())
        computers[b].append((s, a))

    dijkstra((0, c))

    for i in range(1, n + 1):
        if times[i] == 21e8:
            continue
        else:
            cnt += 1

            if times[i] > time:
                time = times[i]

    print(cnt, time)