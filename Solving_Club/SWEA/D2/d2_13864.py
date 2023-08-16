def tmt(g):
    l = len(g)

    if l < 2:
        return g[0]

    if l % 2 == 0:
        m = l // 2
    else:
        m = l // 2 + 1

    g1, g2 = g[:m], g[m:]
    a, b = tmt(g1), tmt(g2)

    if rsp(a, b):
        return a
    else:
        return b


def rsp(x, y):
    game = x[0] - y[0]

    if game == 1 or game == 0 or game == -2:
        return True

    return False


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    card = list(map(int, input().split()))
    player = [(i, idx) for idx, i in enumerate(card, start=1)]

    print(f'#{case} {tmt(player)[1]}')
