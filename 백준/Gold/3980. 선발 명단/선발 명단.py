def recursion(level, sum):
    global res

    if level == 11:
        if res < sum:
            res = sum
        return

    for i in range(11):
        if players[level][i] != 0 and position[i] == 0:
            position[i] = 1
            recursion(level + 1, sum + players[level][i])
            position[i] = 0


test_case = int(input())

for case in range(1, test_case + 1):
    players = [list(map(int, input().split())) for _ in range(11)]
    position = [0] * 11
    res = 0

    for i in range(11):
        if players[0][i] != 0:
            position[i] = 1
            recursion(1, players[0][i])
            position[i] = 0

    print(res)
