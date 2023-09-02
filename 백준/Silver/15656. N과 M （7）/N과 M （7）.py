import sys
input = sys.stdin.readline


def recursion(level):
    if level == m:
        print(*path)
        return

    for i in range(n):
        path[level] = numbers[i]
        recursion(level + 1)


n, m = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))
path = [0] * m
recursion(0)
