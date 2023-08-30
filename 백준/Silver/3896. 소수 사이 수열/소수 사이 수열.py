import sys
input = sys.stdin.readline

end = 1299709
is_prime = [1, 1] + [0] * (end - 1)
prime = []

for i in range(2, end + 1):
    if is_prime[i] == 0:
        prime.append(i)

        for j in range(i * 2, end + 1, i):
            is_prime[j] = 1

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    x, y = 0, 0

    for i in range(len(prime)):
        if prime[i] == n:
            break
        elif prime[i] > n:
            if i - 1 >= 0:
                x = prime[i - 1]
            y = prime[i]
            break

    if x == 0:
        print(0)
    else:
        print(y - x)
