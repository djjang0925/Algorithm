import sys
input = sys.stdin.readline


def dfs(n1, n2):
    stack = [n1]
    check[n1] = 1

    while stack:
        n = stack.pop()

        for i in graph[n]:
            if i == n2:
                print(i)
                return
            check[i] = 1
            stack.append(i)
    
    stack = [n2]

    while stack:
        n = stack.pop()
        
        for i in graph[n]:
            if check[i] == 1:
                print(i)
                return
            stack.append(i)


for case in range(int(input())):
    n = int(input())
    graph = {i: [] for i in range(1, n + 1)}
    check = {i: 0 for i in range(1, n + 1)}

    for i in range(n - 1):
        a, b = map(int, input().rstrip().split())
        graph[b].append(a)

    x, y = map(int, input().rstrip().split())

    dfs(x, y)