from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
perm = sorted(permutations(numbers, m))

for i in perm:
    print(*i)
