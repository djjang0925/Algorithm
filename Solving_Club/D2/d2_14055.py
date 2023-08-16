from collections import deque


def bfs(root, goal):
    global cnt
    visited = [0] * (v + 1)
    q = deque([(root, 0)])

    while q:
        n = q.popleft()

        if n[0] == goal:
            return n[1]

        if visited[n[0]] == 0:
            visited[n[0]] = 1

            for num in graph[n[0]]:
                q.append((num, n[1] + 1))

    return 0


test_case = int(input())

for case in range(1, test_case + 1):
    v, e = map(int, input().split())
    graph = {i: [] for i in range(1, v + 1)}
    cnt = 0

    for i in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    r, g = map(int, input().split())

    print(f'#{case} {bfs(r, g)}')
