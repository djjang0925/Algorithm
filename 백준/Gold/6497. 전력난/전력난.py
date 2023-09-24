import sys
input = sys.stdin.readline


def find(x):
    if houses[x] == x:
        return x

    houses[x] = find(houses[x])

    return houses[x]


def union(x, y):
    f_x, f_y = find(x), find(y)

    if f_x < f_y:
        houses[f_y] = f_x
    else:
        houses[f_x] = f_y


while 1:
    m, n = map(int, input().rstrip().split())

    if [m, n] == [0, 0]:
        break

    houses = {i: i for i in range(m)}
    roads = [list(map(int, input().rstrip().split())) for _ in range(n)]
    roads.sort(key=lambda x: x[2])
    res = 0
    
    for i in roads:
        s, e, c = i

        if find(s) != find(e):
            union(s, e)
        else:
            res += c

    print(res)