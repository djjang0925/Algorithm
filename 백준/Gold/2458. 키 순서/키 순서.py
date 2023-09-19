import sys
input = sys.stdin.readline


def goal(x):
    stack1 = [x]
    stack2 = [x]
    visited = [0] * (n + 1)
    visited[x] = 1

    while stack1:
        now = stack1.pop()

        for i in range(len(graph_2[now])):
            if visited[graph_2[now][i]] == 0:
                visited[graph_2[now][i]] = 1
                stack1.append(graph_2[now][i])

    while stack2:
        now = stack2.pop()

        for i in range(len(graph_1[now])):
            if visited[graph_1[now][i]] == 0:
                visited[graph_1[now][i]] = 1
                stack2.append(graph_1[now][i])

    return visited.count(1)


n, m = map(int, input().rstrip().split())
graph_1 = {i: [] for i in range(1, n + 1)}
graph_2 = {i: [] for i in range(1, n + 1)}
res = 0

for i in range(m):
    a, b = map(int, input().split())
    graph_1[a].append(b)
    graph_2[b].append(a)

for i in range(1, n + 1):
    if goal(i) == n:
        res += 1

print(res)