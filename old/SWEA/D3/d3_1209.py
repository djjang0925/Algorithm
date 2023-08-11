import copy


def dia_sum(x):
    res_d = 0
    dia = copy.deepcopy(x)

    for k in range(2):
        temp_d = 0
        for i in range(100):
            temp_d += dia[i][i]

        if temp_d > res_d:
            res_d = temp_d

        dia = list(map(list, zip(*x[::-1])))

    return res_d


def row_sum(x):
    res_r = 0
    row = copy.deepcopy(x)

    for i in range(2):
        for j in range(100):
            temp_r = sum(row[j])

            if temp_r > res_r:
                res_r = temp_r

        row = list(map(list, zip(*row[::-1])))

    return res_r


for case in range(1, 11):
    n = int(input())
    test_list = [list(map(int, input().split())) for _ in range(100)]
    res = 0

    # 대각선 합 체크
    temp = dia_sum(test_list)
    if temp > res:
        res = temp

    # 가로세로 합 체크
    temp = row_sum(test_list)
    if temp > res:
        res = temp

    print(f'#{case} {res}')
