import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[0] * n for _ in range(n)]
res = 0

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    s = sum(graph[i])
    l = sum([1 if graph[j][i] == 1 else 0 for j in range(n)])

    if s + l == n - 1:
        res += 1

print(res)