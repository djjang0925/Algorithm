test_case = int(input())

for case in range(1, test_case + 1):
    time = list(map(int, input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour > 12:
        hour -= 12
    
    print(f'#{case} {hour} {minute}')
