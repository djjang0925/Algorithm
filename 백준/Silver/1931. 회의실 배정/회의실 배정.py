n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort(key=lambda x: x[0])
graph.sort(key=lambda x: x[1])
res = 1
now = graph[0]

for i in range(1, n):
    if now[1] <= graph[i][0]:
        now = graph[i]
        res += 1

print(res)