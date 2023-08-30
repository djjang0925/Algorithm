import sys
input = sys.stdin.readline


def cnt_2(x):
    c = 0

    while x != 0:
        x //= 2
        c += x

    return c


def cnt_5(x):
    c = 0

    while x != 0:
        x //= 5
        c += x

    return c


n, m = map(int, input().rstrip().split())
c2, c5 = 0, 0

c2 += cnt_2(n)
c2 -= cnt_2(m)
c2 -= cnt_2(n - m)

c5 += cnt_5(n)
c5 -= cnt_5(m)
c5 -= cnt_5(n - m)

print(min(c2, c5))
