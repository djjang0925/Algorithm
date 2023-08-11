from collections import deque


def bfs(start, end):
    global tmap
    queue = deque([start])

    while queue:
        n = queue.popleft()

        next_route = [n+1, n-1, n*2]

        for _ in next_route:
            try:
                if tmap[_] == 0:
                    tmap[_] = tmap[n] + 1
                    queue.append(_)
                elif tmap[_] > tmap[n] + 1:
                    tmap[_] = tmap[n] + 1
                    queue.append(_)
            except IndexError:
                continue

    return tmap[end]


n, k = map(int, input().split())

tmap = [0]*200_001

if n == k:
    print(0)
else:
    print(bfs(n, k))
