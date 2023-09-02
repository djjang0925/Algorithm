from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))
perm = sorted(set(combinations(numbers, m)))

for i in perm:
    print(*i)
