test_case = int(input())

for case in range(1, test_case + 1):
    date = list(map(int, input().split()))
    res = 0
    day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if date[0] == date[2]:
        res = date[3] - date[1] + 1

    else:
        for i in range(date[0], date[2]):
            res += day[i]
        
        res = res - date[1] + date[3] + 1

    print(f'#{case} {res}')