from collections import deque
import sys
input = sys.stdin.readline


def bfs(r, g):
    res = 0
    visited = []
    q = deque([r])

    while q:
        for i in range(len(q)):
            now = q.popleft()

            if now not in visited:
                visited.append(now)

                for j in family[now]:
                    if j == g:
                        print(res + 1)
                        return

                    q.append(j)

        res += 1

    print(-1)


n = int(input())
a, b = map(int, input().rstrip().split())
family = {i: [] for i in range(1, n + 1)}

for i in range(int(input())):
    x, y = map(int, input().rstrip().split())
    family[x].append(y)
    family[y].append(x)

bfs(a, b)
