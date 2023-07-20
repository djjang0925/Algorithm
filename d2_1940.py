test_case = int(input())

for case in range(1, test_case + 1):
    res = 0
    spd = 0
    sec = int(input())

    for i in range(sec):
        move = list(map(int, input().split()))

        if move[0] == 1:
            spd += move[1]
            res += spd
        elif move[0] == 0:
            res += spd
        elif move[0] == 2:
            if spd >= move[1]:
                spd -= move[1]
                res += spd
            else:
                spd = 0

    print(f'#{case} {res}')
