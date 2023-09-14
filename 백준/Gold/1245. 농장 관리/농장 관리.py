from collections import deque
import sys
input = sys.stdin.readline


def bfs(root):
    q = deque([root])
    visited = [[0] * m for _ in range(n)]
    visited[root[0]][root[1]] = 1

    while q:
        y, x = q.popleft()

        for i in direct:
            ny = y + i[0]
            nx = x + i[1]

            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == 1:
                    continue

                if graph[ny][nx] > graph[y][x]:
                    return False
                elif graph[ny][nx] == graph[y][x]:
                    visited[ny][nx] = 1
                    same[ny][nx] = 1
                    q.append([ny, nx])
                else:
                    visited[ny][nx] = 1

    return True


n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
same = [[0] * m for _ in range(n)]
direct = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]]
cnt = 0

for i in range(n):
    for j in range(m):
        if same[i][j] == 0:
            if bfs([i, j]) is True:
                cnt += 1

print(cnt)