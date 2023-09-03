from collections import deque


def service(root):
    global res
    graph = [[0] * n for _ in range(n)]
    graph[root[0]][root[1]] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    home = city[root[0]][root[1]]
    q = deque([root])
    k = 1

    while q:
        if m * home - (k * k + (k - 1) * (k - 1)) >= 0:
            res = max(res, home)

        for i in range(len(q)):
            y, x = q.popleft()

            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]

                if 0 <= ny < n and 0 <= nx < n:
                    if graph[ny][nx] == 1:
                        continue

                    if city[ny][nx] == 1:
                        home += 1
                    graph[ny][nx] = 1
                    q.append([ny, nx])

        k += 1


test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n):
            service([i, j])

    print(f'#{case} {res}')
