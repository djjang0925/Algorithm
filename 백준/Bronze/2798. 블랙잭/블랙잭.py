import sys
input = sys.stdin.readline


def black_jack(level, hand, start):
    if level == 3:
        if hand <= m:
            res.append(hand)
        return

    for i in range(start, n):
        black_jack(level + 1, hand + cards[i], i + 1)


n, m = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))
res = []

black_jack(0, 0, 0)

print(max(res))
