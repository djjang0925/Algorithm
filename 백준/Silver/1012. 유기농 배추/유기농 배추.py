from collections import deque


def bfs(graph, root, y, x):
    global cnt
    cnt += 1
    queue = deque([root])
    m_y = [-1, 1, 0, 0]
    m_x = [0, 0, -1, 1]

    while queue:
        s = queue.popleft()

        if s not in visited:
            visited.append(s)

            for i in range(4):
                n_y = s[0] + m_y[i]
                n_x = s[1] + m_x[i]

                if (0 <= n_y < y) and (0 <= n_x < x) and (graph[n_y][n_x] == 1):
                    queue.append([n_y, n_x])


test_case = int(input())

for case in range(test_case):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    res = []
    visited = []
    cnt = 0

    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] += 1

    for i in range(n):
        for j in range(m):
            if [i, j] not in visited and field[i][j] == 1:
                bfs(field, [i, j], n, m)

    print(cnt)
