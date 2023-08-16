test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    fly_list = []
    max_kill = 0

    for i in range(n):
        fly_list.append(list(map(int, input().split())))

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            dead_fly = 0

            for x in range(i, i + m):
                for y in range(j, j + m):

                    dead_fly += fly_list[x][y]

            if max_kill < dead_fly:

                max_kill = dead_fly

    print(f'#{case} {max_kill}')
