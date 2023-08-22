import sys
input = sys.stdin.readline


graph = [[0] * 100 for _ in range(100)]
res = 0

for i in range(4):
    x, y, gx, gy = map(int, input().rstrip().split())

    for j in range(x, gx):
        for k in range(y, gy):
            if graph[k][j] == 0:
                graph[k][j] = 1
                res += 1

print(res)
