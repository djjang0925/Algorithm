def gcd(x, y):
    while y:
        temp = x
        x = y
        y = temp % x

    return x


n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()
temp = []

a = numbers[1] - numbers[0]

for i in range(2, n):
    a = gcd(numbers[i] - numbers[i - 1], a)

res = [a]

for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        res.append(i)
        res.append(a // i)

print(*sorted(set(res), key=lambda x: x))
