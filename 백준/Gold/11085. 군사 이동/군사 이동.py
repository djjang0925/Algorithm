import sys
input = sys.stdin.readline


def find(x):
    if u[x] == x:
        return x

    u[x] = find(u[x])

    return u[x]


def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        u[x] = y
    else:
        u[y] = x


p, w = map(int, input().rstrip().split())
c, v = map(int, input().rstrip().split())

u = {i: i for i in range(p)}
graph = [list(map(int, input().rstrip().split())) for _ in range(w)]
graph.sort(key=lambda x: x[2], reverse=True)
res = 21e8

for i in graph:
    s, e, w = i

    if find(s) != find(e):
        union(s, e)
        res = min(res, w)

    if find(c) == find(v):
        print(res)
        break