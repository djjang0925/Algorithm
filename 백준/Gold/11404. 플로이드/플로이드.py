import sys
input = sys.stdin.readline

n, m = [int(input()) for _ in range(2)]
graph = [[21e8] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 21e8:
            graph[i][j] = 0

        print(graph[i][j], end=' ')
    print("")