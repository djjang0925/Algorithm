test_case = int(input())

for case in range(1, test_case + 1):
    n, m, l = map(int, input().split())
    tree = {i: 0 for i in range(1, n + 1)}

    for i in range(m):
        j, k = map(int, input().split())
        tree[j] = k

    i = n
    while i > 0:
        if tree[i] == 0:
            left = i * 2
            right = i * 2 + 1

            if right > n:
                tree[i] = tree[left]
            else:
                tree[i] = tree[left] + tree[right]

        i -= 1

    print(f'#{case} {tree[l]}')
