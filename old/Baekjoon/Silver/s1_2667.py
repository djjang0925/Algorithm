from collections import deque


def bfs(graph, root, size):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            check.append(n)
            m_y = [-1, 1, 0, 0]
            m_x = [0, 0, -1, 1]

            for i in range(4):
                n_y = n[0] + m_y[i]
                n_x = n[1] + m_x[i]

                if (0 <= n_y < size) and (0 <= n_x < size) and graph[n_y][n_x] == 1:
                    queue.append([n_y, n_x])

    return len(visited)


n = int(input())
union = [list(map(int, input())) for _ in range(n)]
check = []
cnt = 0
res = []

for i in range(n):
    for j in range(n):
        if [i, j] not in check and union[i][j] == 1:
            res.append(bfs(union, [i, j], n))
            cnt += 1

res.sort()

print(cnt)
for i in range(len(res)):
    print(res[i])
