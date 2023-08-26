test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    numbers = list(i for i in range(31))
    numbers[0] = 1

    for i in range(1, 31):
        numbers[i] *= numbers[i - 1]

    res = numbers[m] // (numbers[m - n] * numbers[n])

    print(res)
