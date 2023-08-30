def find(m):
    if u[m] == 0:
        return m

    ret = find(u[m])
    u[m] = ret

    return ret


def union(x, y):
    f_x, f_y = find(x), find(y)

    if f_x == f_y:
        return

    u[f_y] = f_x


n, m = [int(input()) for _ in range(2)]
u = {i: 0 for i in range(1, n + 1)}

for i in range(1, n + 1):
    cities = [0] + list(map(int, input().split()))

    for j in range(1, n + 1):
        if cities[j] == 1:
            union(i, j)

travel = list(map(int, input().split()))
flag = False

boss = find(travel[0])
for i in range(1, m):
    if find(travel[i]) != boss:
        print('NO')
        break
else:
    print('YES')
