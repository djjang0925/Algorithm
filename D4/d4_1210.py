def ladder_game(x):
    stack = [x]
    res = 0

    while stack:
        n = stack.pop()

        if n[0] == 0:
            res += n[1]
            break

        if ladder[n[0]][n[1]] != 3:
            ladder[n[0]][n[1]] = 3
            dy = [-1, 0, 0]
            dx = [0, -1, 1]

            for i in range(3):
                ny = n[0] + dy[i]
                nx = n[1] + dx[i]

                if (0 <= ny) and (0 <= nx < 100) and (ladder[ny][nx] == 1):
                    stack.append([ny, nx])

    return res


for case in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            print(f'#{case} {ladder_game([99, i])}')
            break
