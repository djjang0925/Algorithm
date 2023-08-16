from collections import deque


def bfs(root):
    q = deque([root])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        graph[y][x] = 4

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 100 and 0 <= nx < 100:
                if graph[ny][nx] == 0:
                    q.append([ny, nx])
                elif graph[ny][nx] == 3:
                    return 1

    return 0


for c in range(1, 11):
    case = int(input())
    graph = [list(map(int, input())) for _ in range(100)]
    r = []
    flag = False

    for i in range(100):
        for j in range(100):
            if graph[i][j] == 2:
                r = [i, j]
                flag = True
                break
        if flag is True:
            break

    res = bfs(r)

    print(f'#{case} {res}')
