from collections import deque
from itertools import combinations

import sys
input = sys.stdin.readline


def bfs(r):
    q = deque([r[0]])
    visited = [r[0]]
    population = 0

    while q:
        n = q.popleft()
        population += populations[n]

        for i in villages[n]:
            if i in r and i not in visited:
                q.append(i)
                visited.append(i)
    return [population, len(visited)]


n = int(input())
populations = [0] + list(map(int, input().rstrip().split()))
villages = {i: [] for i in range(1, n + 1)}
res = 21e8

for i in range(1, n + 1):
    temp = list(map(int, input().rstrip().split()))

    if len(temp) == 1:
        continue
    else:
        villages[i].extend(temp[1:])

for i in range(1, n // 2 + 1):
    combi = list(combinations(range(1, n + 1), i))

    for c in combi:
        temp1 = bfs(c)
        temp2 = bfs([i for i in range(1, n + 1) if i not in c])

        if temp1[1] + temp2[1] == n:
            res = min(res, abs(temp1[0] - temp2[0]))

if res == 21e8:
    print(-1)
else:
    print(res)