import sys
input = sys.stdin.readline


def paint(a, b):
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] = 1


def count(a, b):
    global cnt
    temp = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        ny = a + dy[i]
        nx = b + dx[i]

        if 0 <= ny < 101 and 0 <= nx < 101:
            if graph[ny][nx] == 1:
                temp += 1

    cnt += temp


n = int(input())
graph = [[0] * 102 for _ in range(102)]
cnt = 0
x = []
y = []

for i in range(n):
    n_x, n_y = map(int, input().rstrip().split())
    paint(n_y, n_x)

for i in range(101):
    for j in range(101):
        if graph[i][j] == 0:
            count(i, j)

print(cnt)
