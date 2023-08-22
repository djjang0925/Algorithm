from collections import deque
import sys
input = sys.stdin.readline

def find(y, x):
    global line

    if bingo[y] == [0, 0, 0, 0, 0]:
        line += 1

    if list(list(zip(*bingo))[x]) == [0, 0, 0, 0, 0]:
        line += 1

    if [y, x] in diagonal_1:
        for i in diagonal_1:
            if bingo[i[0]][i[1]] != 0:
                break
        else:
            line += 1

    if [y, x] in diagonal_2:
        for i in diagonal_2:
            if bingo[i[0]][i[1]] != 0:
                break
        else:
            line += 1


bingo = [list(map(int, input().rstrip().split())) for _ in range(5)]
diagonal_1 = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
diagonal_2 = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]
moderator = deque()
line = 0
cnt = 0

for i in range(5):
    moderator.extend(list(map(int, input().rstrip().split())))

while moderator:
    now = moderator.popleft()

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == now:
                bingo[i][j] = 0
                cnt += 1
                find(i, j)

    if line >= 3:
        print(cnt)
        break
