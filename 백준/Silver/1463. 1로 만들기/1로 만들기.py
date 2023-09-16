import sys
input = sys.stdin.readline

n = int(input())
graph = {i: 0 for i in range(1, n + 1)}

for i in range(2, n + 1):
    graph[i] = graph[i - 1] + 1

    if i % 2 == 0:
        graph[i] = min(graph[i], graph[i // 2] + 1)
    if i % 3 == 0:
        graph[i] = min(graph[i], graph[i // 3] + 1)

print(graph[n])