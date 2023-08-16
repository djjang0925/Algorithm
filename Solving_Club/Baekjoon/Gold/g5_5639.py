import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(s, e):
    if s > e:
        return

    root = tree[s]
    index = s + 1

    while index <= e:
        if tree[index] > root:
            break
        index += 1

    post_order(s + 1, index - 1)
    post_order(index, e)
    print(root)


tree = []
while 1:
    try:
        tree.append(int(input()))
    except:
        break

post_order(0, len(tree) - 1)
