from collections import deque

import sys
input = sys.stdin.readline


def turn(cur, nxt):
    if cur == u:
        if nxt == 'D':
            return r
        if nxt == 'L':
            return l
    if cur == d:
        if nxt == 'D':
            return l
        if nxt == 'L':
            return r
    if cur == r:
        if nxt == 'D':
            return d
        if nxt == 'L':
            return u
    if cur == l:
        if nxt == 'D':
            return u
        if nxt == 'L':
            return d


def game():
    q = deque([[0, 0]])
    now = r
    res = 0

    while 1:
        res += 1
        y, x = q[-1]
        ny = y + now[0]
        nx = x + now[1]

        if ny < 0 or ny >= n or nx < 0 or nx >= n or graph[ny][nx] == 1:
            return res

        if graph[ny][nx] == 0:
            ty, tx = q.popleft()
            graph[ty][tx] = 0

        graph[ny][nx] = 1
        q.append([ny, nx])

        if time[res] == '':
            continue
        else:
            now = turn(now, time[res])

    return res


n = int(input())
graph = [[0] * n for _ in range(n)]
graph[0][0] = 1
command = deque([])
u, d, r, l = [-1, 0], [1, 0], [0, 1], [0, -1]
time = [''] * 10_000

for i in range(int(input())):
    y, x = map(int, input().rstrip().split())
    graph[y - 1][x - 1] = 2

for i in range(int(input())):
    a, b = input().rstrip().split()
    time[int(a)] = b

print(game())