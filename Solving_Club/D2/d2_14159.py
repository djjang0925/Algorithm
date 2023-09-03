from collections import deque


def game(p):
    if p[0] == 3:
        return turn

    cnt = 1
    for i in range(1, 10):
        if p[i] == 3:
            return turn

        if p[i - 1] != 0 and p[i] != 0:
            cnt += 1
            if cnt == 3:
                return turn
        else:
            cnt = 1

    return 7


for case in range(1, int(input()) + 1):
    cards = deque(map(int, input().split()))
    player_1 = {i: 0 for i in range(10)}
    player_2 = {i: 0 for i in range(10)}
    turn = 0
    p1, p2 = 7, 7
    print(f'#{case}', end=' ')
    while cards:
        turn += 1
        player_1[cards.popleft()] += 1
        player_2[cards.popleft()] += 1

        p1 = game(player_1)

        if p1 < p2:
            print(1)
            break

        p2 = game(player_2)

        if p1 > p2:
            print(2)
            break
    else:
        print(0)
