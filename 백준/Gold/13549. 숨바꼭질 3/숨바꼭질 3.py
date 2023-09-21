import heapq

n, m = map(int, input().split())
heap = [(0, n)]
visited = [21e8] * 200_000
move = [-1, 1]
visited[n] = 0

while heap:
    time, now = heapq.heappop(heap)

    if now == m:
        print(time)
        break

    for i in range(3):
        n_time, nxt = 0, 0

        if i == 2:
            nxt = now * 2
            n_time = time
        else:
            nxt = now + move[i]
            n_time = time + 1

        if 0 <= nxt < 200_000:
            if n_time < visited[nxt]:
                visited[nxt] = n_time
                heapq.heappush(heap, (n_time, nxt))