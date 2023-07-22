test_case = int(input())

for case in range(1, test_case + 1):
    sdk = []
    res = 0

    for i in range(9):
        sdk.append(list(map(int, input().split())))

    # 가로 비교
    for i in range(9):
        wid = [0] * 10              # 인덱스 넘버를 통한 비교
        for j in range(9):
            wid[sdk[i][j]] += 1
        for j in range(1, 10):
            if wid[i] == 0:
                res = -1
                break

    # 세로 비교
    for i in range(9):
        wid = [0] * 10              
        for j in range(9):
            wid[sdk[j][i]] += 1
        for j in range(1, 10):
            if wid[i] == 0:
                res = -1
                break

    # 3*3 비교
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        temp[i] = sdk[i][:3]
    
    for i in range(3):
        print(*temp[i])