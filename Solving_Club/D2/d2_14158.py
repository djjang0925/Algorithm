test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    trucks = [list(map(int, input().split())) for _ in range(n)]
    trucks.sort(key=lambda x: x[1] - x[0])
    time_table = {i: 0 for i in range(24)}
    cnt = 0

    for i in trucks:
        s, e = i

        for j in range(s, e):
            if time_table[j] != 0:
                break
        else:
            cnt += 1
            for j in range(s, e):
                time_table[j] = cnt

    print(f'#{case} {cnt}')
