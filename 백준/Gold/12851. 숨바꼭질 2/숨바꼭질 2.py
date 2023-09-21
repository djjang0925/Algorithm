import heapq

n, m = map(int, input().split())
heap = [(0, n)]
visited = [21e8] * 200_000
move = [-1, 1]
visited[n] = 0
res = [0, 0]

while heap:
    time, now = heapq.heappop(heap)

    if now == m:
        if res[0] == 0:
            res = [time, 1]
        else:
            if res[0] == time:
                res[1] += 1

    for i in range(3):
        if i == 2:
            nxt = now * 2
        else:
            nxt = now + move[i]

        n_time = time + 1

        if 0 <= nxt < 200_000:
            if n_time <= visited[nxt]:
                visited[nxt] = n_time
                heapq.heappush(heap, (n_time, nxt))

for i in res:
    print(i)