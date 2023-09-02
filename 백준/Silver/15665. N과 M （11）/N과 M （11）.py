import sys
input = sys.stdin.readline


def recursion(level):
    if level == m:
        res.append(tuple(path.copy()))
        return

    for i in range(n):
        path[level] = numbers[i]
        recursion(level + 1)


n, m = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))
path = [0] * m
used = {i: 0 for i in numbers}
res = []

recursion(0)

ans = sorted(set(res))

for i in ans:
    print(*i)
