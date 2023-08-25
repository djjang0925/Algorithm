test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    numbers = {i: 0 for i in range(10)}
    res = 1

    while 1:
        number = n * res
        temp = list(str(number))

        for i in temp:
            numbers[int(i)] += 1

        for i in numbers:
            if numbers[i] == 0:
                break
        else:
            break

        res += 1

    print(f'#{case} {res * n}')
