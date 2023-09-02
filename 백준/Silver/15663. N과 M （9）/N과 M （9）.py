from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = sorted(list(map(int, input().rstrip().split())))
perm = sorted(set(permutations(numbers, m)))

for i in perm:
    print(*i)
