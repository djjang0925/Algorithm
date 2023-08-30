import sys
input = sys.stdin.readline


def find(m):
    if u[m] == 0:
        return m

    ret = find(u[m])
    u[m] = ret

    return ret


def union(x, y, c):
    global res

    f_x, f_y = find(x), find(y)

    if f_x == f_y:
        return

    res += c
    u[f_y] = f_x


n, m = [int(input()) for _ in range(2)]
u = {i: 0 for i in range(1, n + 1)}
graph = []
res = 0

for i in range(m):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])

for i in graph:
    a, b, c = i
    union(a, b, c)

print(res)
