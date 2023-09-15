import math
from collections import deque

n = int(input())
opinions = deque(sorted([int(input()) for _ in range(n)], key=lambda x: x))


if n == 0:
    print(0)
else:
    temp = float(n * 0.15)

    if temp % 1 >= 0.5:
        temp = math.ceil(temp)
    else:
        temp = math.floor(temp)

    for i in range(temp):
        opinions.pop()
        opinions.popleft()

    avg = sum(opinions) / (n - temp * 2)

    if avg % 1 >= 0.5:
        avg = math.ceil(avg)
    else:
        avg = math.floor(avg)

    print(avg)