from collections import deque


def bfs(graph, root, y, x):
    queue = deque(root)
    res = []

    while queue:
        n = queue.popleft()
        m_y = [-1, 1, 0, 0]
        m_x = [0, 0, -1, 1]

        for i in range(4):
            n_y = n[0] + m_y[i]
            n_x = n[1] + m_x[i]

            if (0 <= n_y < y) and (0 <= n_x < x) and (graph[n_y][n_x] == 0):
                queue.append([n_y, n_x])
                graph[n_y][n_x] = graph[n[0]][n[1]] + 1
                res.append(graph[n[0]][n[1]] + 1)

    if len(res) != 0:
        return max(res) - 1
    else:
        return 0


m, n = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
start = []
day = -1
flag = False

for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            start.append([i, j])

res = bfs(field, start, n, m)

for _ in field:
    for tomato in _:
        if tomato == 0:
            print(-1)
            flag = True
            break
    if flag == True:
        break
else:
    print(res)
