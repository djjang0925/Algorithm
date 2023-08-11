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
    g1 = x[:e//2]
    if len(g1) != 2:
    g2 = x[e//2:]


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    card = deque(map(int, input().split()))
    participants = {card[i - 1]: i for i in range(1, n + 1)}








