import sys
sys.setrecursionlimit(int(21e8))
input = sys.stdin.readline


def dfs(r, d):
    for i in graph[r]:
        cur, dis = i
        if distance[cur] == -1:
            distance[cur] = d + dis
            dfs(cur, d+dis)


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for i in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = {i: -1 for i in range(1, n + 1)}
distance[1] = 0
dfs(1, 0)

start = list(distance.values()).index(max(list(distance.values()))) + 1

distance = {i: -1 for i in range(1, n + 1)}
distance[start] = 0
dfs(start, 0)

print(max(list(distance.values())))
