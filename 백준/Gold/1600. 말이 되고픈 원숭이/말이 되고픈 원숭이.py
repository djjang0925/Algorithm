from collections import deque

import sys
input = sys.stdin.readline


def bfs(root):
    q = deque([root])
    visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]
    visited[0][root[0]][root[1]] = 1
    temp = []

    while q:
        y, x, c = q.popleft()

        if [y, x] == [h - 1, w - 1]:
            print(visited[c][y][x] - 1)
            return

        if c < k:
            for i in range(8):
                ny = y + horse[i][0]
                nx = x + horse[i][1]

                if 0 <= ny < h and 0 <= nx < w:
                    if graph[ny][nx] != 0 or visited[c + 1][ny][nx] != 0:
                        continue
                        
                    visited[c + 1][ny][nx] = visited[c][y][x] + 1
                    q.append([ny, nx, c + 1])

        for i in range(4):
            ny = y + move[i][0]
            nx = x + move[i][1]

            if 0 <= ny < h and 0 <= nx < w:
                if graph[ny][nx] != 0 or visited[c][ny][nx] != 0:
                    continue
                    
                visited[c][ny][nx] = visited[c][y][x] + 1
                q.append([ny, nx, c])
    else:
        print(-1)
        return


k = int(input())
w, h = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(h)]
horse = [[2, 1], [1, 2], [-2, 1], [1, -2], [2, -1], [-1, 2], [-2, -1], [-1, -2]]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

bfs([0, 0, 0])