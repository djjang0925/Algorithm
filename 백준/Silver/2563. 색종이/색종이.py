import sys
input = sys.stdin.readline

n = int(input())
c_papers = []
max_x = 0
max_y = 0
res = 0

for i in range(n):
    x, y = map(int, input().rstrip().split())
    c_papers.append([y, x])
    if x + 10 > max_x:
        max_x = x + 10
    if y + 10 > max_y:
        max_y = y + 10

graph = [[0] * max_x for _ in range(max_y)]

for i in range(n):
    y, x = c_papers[i]

    for j in range(y, y + 10):
        for k in range(x, x + 10):
            if graph[j][k] == 0:
                graph[j][k] = 1
                res += 1

print(res)
