from collections import deque


def bfs(root):
    q = deque([root])
    visited = [0] * (n + 1)
    visited[root[0]] = 1

    while q:
        now, cnt = q.popleft()

        if cnt == k:
            res.append(now)
            continue

        if graph[now]:
            for i in range(len(graph[now])):
                if visited[graph[now][i]] == 0:
                    visited[graph[now][i]] = 1
                    q.append([graph[now][i], cnt + 1])


n, m, k, x = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
res = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs([x, 0])

res.sort()
if res:
    for i in res:
        print(i)
else:
    print(-1)