test_case = int(input())

for case in range(1, test_case + 1):
    tree = input()
    l, r = 1, 1

    for i in range(len(tree)):
        if tree[i] == 'L':
            r += l
        else:
            l += r

    print(f'#{case} {l} {r}')