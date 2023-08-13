import sys
input = sys.stdin.readline


def dfs(r):
    global res
    stack = [r]

    if visited[r-1] == 0:
        return

    while stack:
        n = stack.pop()

        if visited[n-1] != 0:
            visited[n-1] = 0
            stack.extend(graph_dict[n])

    res += 1

    return


n, m = map(int, input().rstrip().split())
graph_dict = {i: [] for i in range(1, n + 1)}
visited = [i for i in range(1, n + 1)]
res = 0

for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph_dict[u].append(v)
    graph_dict[v].append(u)

for i in range(1, n + 1):
    dfs(i)

print(res)
