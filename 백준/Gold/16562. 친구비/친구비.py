def find(x):
    if u[x] == 0:
        return x

    u[x] = find(u[x])

    return u[x]


def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return

    if price[fa] > price[fb]:
        u[fa] = fb
    else:
        u[fb] = fa


n, m, k = map(int, input().split())
price = [0] + list(map(int, input().split()))
u = {i: 0 for i in range(1, n + 1)}
cost = 0
friends = set()

for i in range(m):
    x, y = map(int, input().split())
    union(x, y)

for i in range(1, n + 1):
    if find(i) not in friends:
        cost += price[find(i)]
    friends.add(find(i))

if cost > k:
    print('Oh no')
else:
    print(cost)
