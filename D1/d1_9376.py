test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    carrots = list(map(int, input().split()))
    cnt, res = 1, 0

    for i in range(1, n):
        if carrots[i] > carrots[i - 1]:
            cnt += 1
        else:
            if cnt > res:
                res = cnt
            cnt = 1
    else:
        if cnt > res:
            res = cnt

    print(f'#{case} {res}')
