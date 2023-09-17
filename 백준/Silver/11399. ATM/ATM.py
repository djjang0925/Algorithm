import sys
input = sys.stdin.readline

n = int(input())
people = sorted(list(map(int, input().rstrip().split())), key=lambda x: x)
res = 0

for i in range(n):
    for j in range(0, i + 1):
        res += people[j]

print(res)