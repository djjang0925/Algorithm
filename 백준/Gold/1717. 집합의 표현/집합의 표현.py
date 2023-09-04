import sys
input = sys.stdin.readline


def find(m):
    if u[m] == m:
        return m

    ret = find(u[m])
    u[m] = ret

    return ret


def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return

    u[fb] = fa


n, m = map(int, input().rstrip().split())
u = {i: i for i in range(n + 1)}

for i in range(m):
    command = list(map(int, input().rstrip().split()))

    if command[0] == 0:
        union(command[1], command[2])
    else:
        if find(command[1]) == find(command[2]):
            print('YES')
        else:
            print('NO')
