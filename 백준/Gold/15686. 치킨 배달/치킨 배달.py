def recursion(lv, start):
    global res
    if lv == m:
        calculate(path)
        return

    for i in range(start, len(chicken)):
        path[lv] = chicken[i]
        recursion(lv + 1, i + 1)


def calculate(x):
    global res
    route = [21e8] * len(home)

    for i in range(len(home)):
        for j in x:
            temp = abs(home[i][0]-j[0]) + abs(home[i][1]-j[1])
            if temp < route[i]:
                route[i] = temp

    cnt = sum(route)

    if cnt < res:
        res = cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []
path = [0] * m
res = 21e8

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

recursion(0, 0)

print(res)
