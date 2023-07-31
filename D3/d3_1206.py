def Rov(x):
    buildings_temp = list(buildings[x-2:x+3])

    # print(buildings_temp)

    buildings_temp.sort(reverse=True)
    if buildings[x] == max(buildings_temp):
        return buildings_temp[0] - buildings_temp[1]
    else:
        return 0

test_case = 11

for case in range(1, test_case):
    n = int(input())
    buildings = list(map(int, input().split()))
    res = 0
    for i in range(2, len(buildings) - 2):
        res += Rov(i)

    print(f'#{case} {res}')

