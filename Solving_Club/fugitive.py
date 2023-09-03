from collections import deque


def tunnel(x):
    if x == 1:
        return [[-1, 1, 0, 0], [0, 0, -1, 1], [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]]
    elif x == 2:
        return [[-1, 1], [0, 0], [[1, 2, 5, 6], [1, 2, 4, 7]]]
    elif x == 3:
        return [[0, 0], [-1, 1], [[1, 3, 4, 5], [1, 3, 6, 7]]]
    elif x == 4:
        return [[-1, 0], [0, 1], [[1, 2, 5, 6], [1, 3, 6, 7]]]
    elif x == 5:
        return [[1, 0], [0, 1], [[1, 2, 4, 7], [1, 3, 6, 7]]]
    elif x == 6:
        return [[1, 0], [0, -1], [[1, 2, 4, 7], [1, 3, 4, 5]]]
    elif x == 7:
        return [[-1, 0], [0, -1], [[1, 2, 5, 6], [1, 3, 4, 5]]]


def bfs(root):
    q = deque([root])
    cnt = 1

    while q:
        y, x, t = q.popleft()
        dy, dx, g = tunnel(graph[y][x])

        if t == l:
            continue

        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] in g[i] and hide[ny][nx] == 0:
                    cnt += 1
                    hide[ny][nx] = 1
                    q.append([ny, nx, t + 1])

    return cnt


for case in range(1, int(input()) + 1):
    n, m, r, c, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    hide = [[0] * m for _ in range(n)]
    hide[r][c] = 1

    print(f'#{case} {bfs([r, c, 1])}')
