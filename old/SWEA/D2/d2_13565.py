def next_station(x):
    temp = charge_station.copy()
    temp.reverse()

    for station in temp:
        if station - x <= k:
            return station


test_case = int(input())

for case in range(1, test_case + 1):
    k, n, m = map(int, input().split())
    charge_station = list(map(int, input().split()))
    flag = False
    prev_station = 0
    now = 0
    cnt = 0

    for station in charge_station:
        if station - prev_station > k:
            flag = True
            break
        else:
            prev_station = station
    else:
        if n - prev_station > k:
            flag = True
    
    if flag != True:
        while now + k < n:
            now = next_station(now)
            cnt += 1
        
    if flag == True:
        print(f'#{case} 0')
    else:
        print(f'#{case} {cnt}')
