def recursion(level):
    if level == m:
        print(*res)
        return

    for num in numbers:
        res[level] = num
        recursion(level + 1)


n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
res = [0] * m
recursion(0)
