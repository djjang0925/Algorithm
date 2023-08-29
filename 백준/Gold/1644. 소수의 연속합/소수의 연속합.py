import sys
input = sys.stdin.readline

n = int(input())

if n == 0 or n == 1:
    print(0)
else:
    prime = [0, 0] + [1] * (n - 1)
    num = []

    for i in range(2, n + 1):
        if prime[i] == 1:
            num.append(i)

        for j in range(i * 2, n + 1, i):
            prime[j] = 0

    temp, cnt = 0, 0
    high, low = 0, 0

    while 1:
        if temp >= n or high == len(num):
            temp -= num[low]
            low += 1
        elif temp < n:
            temp += num[high]
            high += 1

        if temp == n:
            cnt += 1

        if low == len(num):
            break

    print(cnt)
