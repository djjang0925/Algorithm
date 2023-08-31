import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
ans = sorted(sorted(arr, key=lambda x: x[0]), key=lambda x: x[1])

for i in ans:
    print(*i)
