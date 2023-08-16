test_case = int(input())
res = ''

for i in range(1, test_case + 1):
    temp = str(input())
    year = int(temp[0:4])
    month = int(temp[4:6])
    day = int(temp[6:8])

    if (month > 12) or (month == 0) or (day == 0):
        print(f'#{i} -1')
    elif (month == 2) and (day > 28):
        print(f'#{i} -1')
    elif (month in [1, 3, 5, 7, 8, 10, 12]) and (day > 31):
        print(f'#{i} -1')
    elif (month in [4, 6, 9, 11]) and (day > 30):
        print(f'#{i} -1')
    else:
        print(f'#{i} {temp[0:4]}/{temp[4:6]}/{temp[6:8]}')