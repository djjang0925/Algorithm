import sys
input = sys.stdin.readline


# 2중 for문 > 슬라이싱 (시간복잡도)
def color(root, goal, paint):
    for i in range(root[0], root[0] + goal[0]):
        graph[i][root[1]:root[1] + goal[1]] = [paint] * goal[1]


n = int(input())
graph = [[0] * 1001 for _ in range(1001)]
colors = {i: 0 for i in range(1, n + 1)}

for i in range(1, n + 1):
    a, b, c, d = map(int, input().rstrip().split())
    color([a, b], [c, d], i)

for i in range(1001):
    for j in range(1001):
        if graph[i][j] != 0:
            colors[graph[i][j]] += 1

for i in colors:
    print(colors[i])
