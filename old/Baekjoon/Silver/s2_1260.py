from pprint import pprint
from collections import deque

n, m, v = map(int, input().split())
graph_list = [[] for _ in range(n)]
graph_dic = {}

# 그래프 딕셔너리 {정점 : 간선(set)}
for i in range(m):
    num1, num2 = map(int, input().split())
    graph_list[num1 - 1].append(num2)
    graph_list[num2 - 1].append(num1)

for i in range(n):
    graph_list[i].sort(reverse=True)
    graph_dic[i + 1] = graph_list[i]

print(graph_dic)

def Dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n]
            # print(visited)
    
    return visited


def Bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        
        if n not in visited:
            visited.append(n)
            graph[n].reverse()
            queue += graph[n]

    return visited

print(*Dfs(graph_dic, v))
print(*Bfs(graph_dic, v))
