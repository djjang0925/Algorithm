def inorder(now):
    if now > n:
        return

    inorder(now * 2)

    print(tree[now], end='')

    inorder(now * 2 + 1)


for case in range(1, 11):
    n = int(input())
    tree = {i: '' for i in range(1, n + 1)}

    for i in range(n):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1]

    print(f'#{case}', end=' ')
    inorder(1)
    print()
