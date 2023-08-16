from collections import deque

pc = int(input())
graph_lists = [[0] for _ in range(pc + 1)]
route = int(input())
graph_dic = {}

for i in range(route):
    num1, num2 = map(int, input().split())
    graph_lists[num1].append(num2)
    graph_lists[num2].append(num1)

for i in range(1, pc + 1):
    graph_lists[i].remove(0)

for i in range(1, pc + 1):
    graph_dic[i] = graph_lists[i]


def Bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    
    print(len(visited) - 1)

Bfs(graph_dic, 1)
