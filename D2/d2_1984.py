from functools import reduce
import math

test_case = int(input())

for case in range(1, test_case + 1):
    numbers = list(map(int, input().split()))
    numbers.pop(numbers.index(max(numbers)))
    numbers.pop(numbers.index(min(numbers)))
    numbers_sum = reduce(lambda x, y: x + y, numbers)
    res = math.floor(numbers_sum / 8 + 0.5)         # 정확한 소수점 계산을 위해 0.5를 더한 후 내림처리

    print(f'#{case} {res}')
