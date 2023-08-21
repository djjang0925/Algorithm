import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline


def game(level, x):
    global temp, res
    if level == n:
        if temp > res:
            res = temp

        temp = 0
        return

    dice = dices[level][:]

    a = dice.index(x)

    if a == 0:
        b = 5
    elif a == 1:
        b = 3
    elif a == 2:
        b = 4
    elif a == 3:
        b = 1
    elif a == 4:
        b = 2
    elif a == 5:
        b = 0

    y = dice[b]
    dice.remove(x)
    dice.remove(y)

    temp += max(dice)

    game(level+1, y)


n = int(input())
dices = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = 0
temp = 0

for i in range(6):
    count = {i: n for i in range(1, 7)}
    game(0, dices[0][i])

print(res)
