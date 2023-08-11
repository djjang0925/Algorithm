import sys
input = sys.stdin.readline


def dfs():
    stack = [r]
    cnt = 1

    while stack:
        n = stack.pop()

        if res[n] == 0:
            res[n] = cnt
            cnt += 1
            stack.extend(test_dict[n])


n, m , r = map(int, input().rstrip().split())
test_dict = {i: [0] for i in range(1, n + 1)}
res = {i: 0 for i in range(1, n + 1)}

for i in range(m):
    s, e = map(int, input().rstrip().split())
    test_dict[s].append(e)
    test_dict[e].append(s)

for i in range(1, n + 1):
    test_dict[i].sort()
    test_dict[i].remove(0)

dfs()
for i in range(1, n + 1):
    print(res[i])
