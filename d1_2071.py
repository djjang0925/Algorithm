from functools import reduce
test_case = int(input())

for i in range(test_case):
    numbers = list(map(int, input().split()))
    avg = reduce(lambda x, y: x + y, numbers) / len(numbers)
    print(f'#{i + 1} {int(round(avg, 0))}')