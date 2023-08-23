def order(o):
    # 다음 명령을 확인 후 다이렉트 배열 리턴
    if o == 'R':
        return [0, 1]
    elif o == 'L':
        return [0, -1]
    elif o == 'B':
        return [-1, 0]
    elif o == 'T':
        return [1, 0]
    elif o == 'RT':
        return [1, 1]
    elif o == 'LT':
        return [1, -1]
    elif o == 'RB':
        return [-1, 1]
    elif o == 'LB':
        return [-1, -1]


king, stone, n = input().split()

# 킹, 돌의 좌표를 0~7기준으로 변경하여 y, x로 할당
y, x = [int(king[1]) - 1, ord(king[0]) - 65]
sy, sx = [int(stone[1]) - 1, ord(stone[0]) - 65]

n = int(n)
move = [input() for _ in range(n)]
chess = [[0] * 8 for _ in range(8)]

# 킹, 돌 체스판에 마킹
chess[y][x] = 1
chess[sy][sx] = 2

for i in range(n):
    # 함수를 통하여 다음 이동경로 받아오기
    dy, dx = order(move[i])

    # 킹의 다음 이동경로 할당
    ny = y + dy
    nx = x + dx

    # 킹의 이동경로가 체스판을 벗어나지 않을 경우
    if 0 <= ny < 8 and 0 <= nx < 8:
        # 킹의 이동방향에 돌이 없는 경우 킹 이동
        if chess[ny][nx] == 0:
            chess[y][x] = 0
            chess[ny][nx] = 1
            y, x = ny, nx
        else:
            # 돌이 있을 경우 돌의 이동경로 할당
            nsy = sy + dy
            nsx = sx + dx

            # 돌의 이동경로가 체스판을 벗어나지 않을 경우
            if 0 <= nsy < 8 and 0 <= nsx < 8:
                chess[sy][sx] = 0
                chess[nsy][nsx] = 2
                chess[y][x] = 0
                chess[ny][nx] = 1
                sy, sx = nsy, nsx
                y, x = ny, nx
        

flag = False
for i in range(1, 3):
    res = ''
    for j in range(8):
        for k in range(8):
            if i == chess[j][k]:
                res += chr(k + 65)
                res += str(j+1)
                flag = True
                break

        if flag is True:
            flag = False
            break

    print(res)
