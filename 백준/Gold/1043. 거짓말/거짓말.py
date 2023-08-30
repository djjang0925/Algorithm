def find(m):
    if u[m] == 0:
        return m

    ret = find(u[m])
    u[m] = ret

    return ret


def union(x, y):
    fx, fy = find(x), find(y)

    if fx == fy:
        return

    u[fy] = fx


n, m = map(int, input().split())
u = {i: 0 for i in range(1, n + 1)}
true = list(map(int, input().split()))

if len(true) == 1:
    print(m)
else:
    parties = []
    res = m

    for i in range(1, true[0]):
        union(true[i], true[i + 1])

    for i in range(m):
        party = list(map(int, input().split()))
        parties.append(party)

        if party[0] == 1:
            continue

        for j in range(1, party[0]):
            union(party[j], party[j + 1])

    boss = find(true[1])
    for party in parties:
        for i in range(1, party[0] + 1):
            if find(party[i]) == boss:
                res -= 1
                break

    print(res)
