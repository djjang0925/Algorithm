from collections import deque


def rcp(x, y):
    if participants[x] == 1 and participants[y] == 3:
        return x
    elif participants[y] == 1 and participants[x] == 3:
        return y
    elif participants[x] > participants[y]:
        return x
    elif participants[y] > participants[x]:
        return y
    elif participants[y] == participants[x]:
        if x < y:
            return x
        else:
            return y


def tmt(x):
    e = len(x)
    if e % 2 == 0:
        m = e // 2
    else:
        m = e // 2 + 1

    g1 = list(x[:m])
    if len(g1) == 2:
        winner.append(rcp(g1[0], g1[1]))
    else:
        tmt(g1)
    g2 = list(x[m:])
    if len(g2) == 1:
        winner.append(g2[0])
        return
    elif len(g2) == 2:
        winner.append(rcp(g2[0], g2[1]))
        return
    else:
        tmt(g2)


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    card = list(map(int, input().split()))
    participants = {card[i - 1]: i for i in range(1, n + 1)}
    winner = []
    tmt(card)

    while 1:






