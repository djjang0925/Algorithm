import math
from itertools import permutations


def is_p_num(x):
    n = int(math.sqrt(x)) + 1

    for i in range(2, n):
        if x % i == 0:
            return False

    return True


def is_p_sum(x):
    for i in p_num:
        if i > x:
            return False

        if is_prime[i] == 1:
            if x - i == i:
                return False

            if is_prime[x - i] == 1:
                return True

    else:
        return False


def is_p_mul(x):
    temp = x

    while temp % m == 0:
        temp //= m

    for i in p_num:
        if i > temp:
            return False

        if temp % i == 0 and is_prime[temp // i] == 1:
            return True

    else:
        return False


k, m = map(int, input().split())
is_prime = {i: 0 for i in range(1, 10**k)}
p_num = []
res = 0

for i in range(2, 10**k):
    if is_p_num(i):
        p_num.append(i)
        is_prime[i] = 1

for perm in permutations(range(10), k):
    if perm[0] == 0:
        continue
    num = int(''.join(list(map(str, perm))))

    if is_p_mul(num) and is_p_sum(num):
        res += 1

print(res)
