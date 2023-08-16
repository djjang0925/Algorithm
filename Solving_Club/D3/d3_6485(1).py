test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    bus = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    station = {}
    station_order = []

    for i in range(p):
        num = int(input())
        station[num] = 0
        station_order.append(num)

    for route in bus:
        for i in range(route[0], route[1] + 1):
            if i in station:
                station[i] += 1

    print(f'#{case}', end=' ')

    for _ in station_order:
        print(station[_], end=' ')

    print('')
