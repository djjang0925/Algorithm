import sys
input = sys.stdin.readline


def color(root, goal, paint):
    for i in range(root[0], goal[0]):
        for j in range(root[1], goal[1]):
            if graph[i][j] != 0:
                colors[graph[i][j]] -= 1
            graph[i][j] = paint
            colors[paint] += 1


n = int(input())
graph = [[0] * 1002 for _ in range(1002)]
colors = {i: 0 for i in range(1, n + 1)}

for i in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    color([a, b], [a + c, b + d], i + 1)

for i in colors:
    print(colors[i])
