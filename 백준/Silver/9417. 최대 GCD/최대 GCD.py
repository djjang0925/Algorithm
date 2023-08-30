from itertools import combinations

test_case = int(input())

for case in range(1, test_case + 1):
    numbers = list(map(int, input().split()))
    com = list(combinations(numbers, 2))
    res = 0

    while com:
        x, y = com.pop()

        while y:
            temp = x
            x = y
            y = temp % y

        if x > res:
            res = x

    print(res)
