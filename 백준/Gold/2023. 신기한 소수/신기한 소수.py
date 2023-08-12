from collections import deque
import math


def prime_num(x):
    queue = deque([x])

    while queue:
        p_num = queue.popleft()

        if 10 ** n <= p_num < 10 ** (n + 1):
            print(p_num // 10)
        elif p_num >= 10 ** (n + 1):
            break

        for i in range(p_num, p_num + 10):
            for j in range(2, math.ceil(p_num ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                queue.append(i * 10)


n = int(input())
start_num = [2, 3, 5, 7]

for num in start_num:
    prime_num(num * 10)
