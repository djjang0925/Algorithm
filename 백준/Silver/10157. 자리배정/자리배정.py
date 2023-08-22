r, c = map(int, input().split())
k = int(input())

if k > c * r:
    print(0)
else:
    hall = [[0] * r for _ in range(c)]
    cnt = 0
    flag = False

    for i in range(c//2):
        for j in range(i, c - i):
            cnt += 1
            hall[j][i] = cnt

            if cnt == k:
                print(i + 1, j + 1)
                flag = True
                break

        if flag is True:
            break

        for j in range(i + 1, r - 1 - i):
            cnt += 1
            hall[c - 1 - i][j] = cnt

            if cnt == k:
                print(j + 1, c - i)
                flag = True
                break

        if flag is True:
            break

        for j in range(c - 1 - i, i, -1):
            cnt += 1
            hall[j][r - 1 - i] = cnt

            if cnt == k:
                print(r - i, j + 1)
                flag = True
                break

        if flag is True:
            break

        for j in range(r - 1 - i, i, -1):
            cnt += 1
            hall[i][j] = cnt

            if cnt == k:
                print(j + 1, i + 1)
                flag = True
                break

        if flag is True:
            break
