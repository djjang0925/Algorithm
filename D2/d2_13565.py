from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    k, n, m = map(int, input().split())
    charge_station = deque(map(int, input().split()))
    flag = False
    now = 0
    cnt = 0

    charge_station.appendleft(0)
    
    if charge_station[-1] != n:
        charge_station.append(n)

    for i in range(len(charge_station) - 1):
        if charge_station[i + 1] - charge_station[i] > k:
            flag = True
            print(f'#{case} 0')
            break
    
    charge_station.popleft()    # 1, 3, 5, 7, 9, 10
    charge_station.pop()        # 1, 3, 5, 7, 9
    charge_station.reverse()    # 9, 7, 5, 3, 1

    while now + k < n:
        battery = now + k

        for i in charge_station:
            if battery >= i:
                cnt += 1
                now = i
                break

    if flag == True:
        print(f'#{case} 0')
    else:
        print(f'#{case} {cnt}')
    



        
    
