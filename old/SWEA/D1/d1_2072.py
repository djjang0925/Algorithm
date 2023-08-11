test_case = int(input())

for i in range(test_case):
    numbers = list(map(int, input().split()))
    res = 0

    for j in range(len(numbers)):
        if numbers[j] % 2 == 1:
            res += numbers[j]

    print(f'#{i + 1} {res}')