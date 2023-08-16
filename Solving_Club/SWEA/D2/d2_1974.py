test_case = int(input())

for case in range(1, test_case + 1):
    sdk = []
    res = 0

    for i in range(9):
        sdk.append(list(map(int, input().split())))

    # 가로 비교
    for i in range(9):
        wid = [0] * 10
        leng = [0] * 10

        for j in range(9):
            wid[sdk[i][j]] += 1
            leng[sdk[j][i]] += 1

            if (wid[sdk[i][j]] > 1) or (leng[sdk[j][i]] > 1):
                res -= 1

    # 3*3 비교
    for i in range(3):
        for j in range(3):
            temp = [0] * 10

            for k in range(3):
                for l in range(3):
                    temp[sdk[i*3 + k][j*3 + l]] += 1

                    if temp[sdk[i*3 + k][j*3 + l]] > 1:
                        res -= 1
                        break

    if res != 0:
        print(f'#{case} 0')
    else:
        print(f'#{case} 1')