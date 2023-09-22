import sys
input = sys.stdin.readline


def recursion(level, temp, pre):
    global ans

    if temp > ans:
        return

    if level == n:
        if temp < ans:
            ans = temp

        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        recursion(level + 1, temp + graph[pre][i], i)
        visited[i] = 0


n, s = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visited = [0] * n
visited[s] = 1
ans = 21e8

recursion(1, 0, s)

print(ans)