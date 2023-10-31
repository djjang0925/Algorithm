import sys
input = sys.stdin.readline


def dfs(r):
    res = 0
    stack = [r]

    while stack:
        now = stack.pop()
        
        if len(graph[now]) == 1 and graph[now][0] == remove_node:
            res += 1
            continue
            
        if graph[now]:
            for i in graph[now]:
                if i == remove_node:
                    continue
                stack.append(i)
        else:
            res += 1

    print(res)


n = int(input())
parents = list(map(int, input().rstrip().split()))
graph = {i: [] for i in range(n)}
root = -1

for i in range(n):
    if parents[i] == -1:
        root = i
        continue

    graph[parents[i]].append(i)

remove_node = int(input())

if root == remove_node:
    print(0)
else:
    dfs(root)