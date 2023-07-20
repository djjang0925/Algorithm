test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    print(f'#{case}', *numbers)