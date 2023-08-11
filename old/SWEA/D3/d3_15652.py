def recursion(level, start):
    if level == m:
        print(*res)
        return

    for i in range(start, n):
        res[level] = numbers[i]
        recursion(level + 1, i)


n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
res = [0] * m
recursion(0, 0)
