import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def post_order(l, r):
    if l <= r:
        root = pre_order[l]
        idx = None

        for i, v in enumerate(pre_order[l + 1:], l + 1):
            if root < v:
                idx = i
                break

        if idx is None:
            idx = r + 1

        post_order(l + 1, idx - 1)
        post_order(idx, r)

        print(root)


pre_order = []

while 1:
    n = input()

    try:
        if n == '':
            break
        else:
            pre_order.append(int(n))
    except:
        break

post_order(0, len(pre_order) - 1)
