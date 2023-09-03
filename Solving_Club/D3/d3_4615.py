def change(y, x, c):
    dy = [-1, 1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, -1, 1, 1, -1, 1, -1]

    for i in range(8):
        temp = []
        for j in range(1, n):
            ny = y + dy[i] * j
            nx = x + dx[i] * j

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 0:
                    break

                if graph[ny][nx] != c:
                    temp.append([ny, nx])
                elif graph[ny][nx] == c:
                    for k in temp:
                        graph[k[0]][k[1]] = c
                    break


test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    graph[n//2][n//2] = 2
    graph[n//2][n//2 - 1] = 1
    graph[n//2 - 1][n//2 - 1] = 2
    graph[n//2 - 1][n//2] = 1

    for i in range(m):
        x, y, t = map(int, input().split())
        y -= 1
        x -= 1

        graph[y][x] = t

        change(y, x, t)

    stone = [0, 0]

    for i in graph:
        stone[0] += i.count(1)
        stone[1] += i.count(2)

    print(f'#{case}', *stone)
