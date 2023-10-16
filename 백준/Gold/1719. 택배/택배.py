import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[21e8] * n for _ in range(n)]
routes = [[0] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
    routes[a - 1][b - 1] = b - 1
    routes[b - 1][a - 1] = a - 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                routes[i][j] = routes[i][k]

for i in range(n):
    routes[i][i] = '-'

for i in range(n):
    for j in range(n):
        if i == j:
            print('-', end=' ')
        else:
            print(routes[i][j] + 1, end=' ')
    print('')