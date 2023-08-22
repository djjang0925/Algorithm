w, h = map(int, input().split())
joi = [list(input()) for _ in range(w)]
res = [[-1] * h for _ in range(w)]

for i in range(w):
    flag = False
    cnt = 0

    for j in range(h):
        if joi[i][j] == 'c':
            flag = True
            cnt = 0

        if flag is True:
            res[i][j] = cnt
            cnt += 1

for i in res:
    print(*i)
