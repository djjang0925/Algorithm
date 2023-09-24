import sys
input = sys.stdin.readline


def find(m):
    if village[m] == 0:
        return m

    village[m] = find(village[m])

    return village[m]


def union(x, y):
    f_x, f_y = find(x), find(y)

    if f_x == f_y:
        return

    if f_x < f_y:
        village[f_x] = f_y
    else:
        village[f_y] = f_x


n, m = map(int, input().rstrip().split())

village = {i: 0 for i in range(1, n + 1)}
bridges = [list(map(int, input().rstrip().split())) for _ in range(m)]
bridges.sort(key=lambda x: x[2])

ans, cost = 0, 0

for i in bridges:
    s, e, c = i

    if find(s) != find(e):
        union(s, e)
        ans += c
        cost = max(cost, c)

print(ans - cost)