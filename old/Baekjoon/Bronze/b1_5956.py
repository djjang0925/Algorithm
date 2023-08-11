def symmetry(y, x):
    global cow, cnt, res

    if y % 2 == 0 or x % 2 == 0:
        return

    res += cow ** cnt

    if (y // 2 < 3 and x // 2 < 1) or (y // 2 < 1 and x // 2 < 3):
        return
    else:
        cnt += 1
        symmetry(y//2, x//2)


cow = 4
cnt = 0
res = 0
n, m = map(int, input().split())
symmetry(n, m)
print(res)
