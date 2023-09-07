from collections import deque
import sys
input = sys.stdin.readline


def bfs(r):
    q = deque([r])

    while q:
        y, x = q.popleft()

        if [y, x] == goal:
            print(chess_board[y][x] - 1)
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < size and 0 <= nx < size:
                if chess_board[ny][nx] == 0:
                    chess_board[ny][nx] = chess_board[y][x] + 1
                    q.append([ny, nx])


for case in range(1, int(input()) + 1):
    size = int(input())
    chess_board = [[0] * size for _ in range(size)]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    knight = list(map(int, input().rstrip().split()))
    goal = list(map(int, input().rstrip().split()))

    chess_board[knight[0]][knight[1]] = 1
    bfs(knight)
   