def c_list(x):
    global flag

    for num in range(1, 10):
        if num not in x:
            flag = True


def c_33(y, x):
    global flag
    temp = []

    for i in range(y, y+3):
        for j in range(x, x+3):
            temp.append(sdk[i][j])

    for num in range(1, 10):
        if num not in temp:
            flag = True

test_case = int(input())

for case in range(1, test_case + 1):
    sdk = [list(map(int, input().split())) for _ in range(9)]
    flag = False

    # 가로체크
    for row in sdk:
        c_list(row)

    # 세로체크
    temp = list(map(list, zip(*sdk[::-1])))
    for col in temp:
        c_list(col)

    # 33체크
    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            c_33(i, j)

    if flag == False:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
