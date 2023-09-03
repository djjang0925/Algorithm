def recursion(y, x, temp):
    global res

    if y == n - 1 and x == n - 1:
        if temp < res:
            res = temp
        return

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            recursion(ny, nx, temp + graph[ny][nx])


for case in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dy = [1, 0]
    dx = [0, 1]
    res = 21e8

    recursion(0, 0, graph[0][0])

    print(f'#{case} {res}')
