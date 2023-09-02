import sys
input = sys.stdin.readline


def recursion(level, start):
    if level == m:
        print(*path)
        return

    for i in range(start, n):
        path[level] = numbers[i]
        recursion(level + 1 , i)


n, m = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))
path = [0] * m
recursion(0, 0)
