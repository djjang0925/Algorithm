import heapq


def dijkstra(s):
    heap = [(0, s)]
    graph[s] = 0

    while heap:
        time, now = heapq.heappop(heap)

        if now == k:
            return time

        if time > graph[now]:
            continue

        for i in range(3):
            if i < 2:
                nxt = now + move[i]
            else:
                nxt = now * move[i]
            n_time = time + 1

            if 0 <= nxt < 100_001 and n_time < graph[nxt]:
                graph[nxt] = n_time
                route[nxt] = now
                heapq.heappush(heap, (n_time, nxt))


n, k = map(int, input().split())
graph = [21e8] * 100_001
move = [-1, 1, 2]
route = {i: i for i in range(100_001)}

print(dijkstra(n))

path = []
while k != n:
    path.append(k)
    k = route[k]

path.append(k)
print(*path[::-1])