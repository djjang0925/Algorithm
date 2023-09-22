import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().rstrip().split())
graph = [[21e8] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = c

c = int(input())
friends = list(map(int, input().rstrip().split()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

d = 21e8
ans = []

for i in range(1, n + 1):
    temp = 0

    for j in friends:
        if i != j and graph[i][j] != 21e8 and graph[j][i] != 21e8:
            temp = max(temp, graph[i][j] + graph[j][i])

    if temp < d:
        d = temp
        ans = [i]
    elif temp == d:
        heapq.heappush(ans, i)

while ans:
    print(heapq.heappop(ans), end=' ')