from collections import deque
import sys


def bfs(graph, root):
    visited = [0] * (n + 1)
    queue = deque([root])

    order = 1
    while queue:
        s = queue.popleft()

        if visited[s] == 0:
            visited[s] = order
            queue.extend(graph[s])
            order += 1

    print(*visited[1:], sep='\n')


n, m, r = map(int, sys.stdin.readline().rstrip().split())
test_graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    test_graph[a].append(b)
    test_graph[b].append(a)

for i in range(1, n + 1):
    test_graph[i].sort()

bfs(test_graph, r)
