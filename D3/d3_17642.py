test_case = int(input())

for case in range(1, test_case + 1):
    num1, num2 = map(int, input().split())

    res = abs(num1 - num2) // 2

    if num2 < num1:
        print(f'#{case} -1')
    elif abs(num1 - num2) == 1:
        print(f'#{case} -1')
    else:
        print(f'#{case} {res}')