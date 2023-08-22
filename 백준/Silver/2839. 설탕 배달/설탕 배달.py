n = int(input())

i = 0
while 1:
    if n % 5 == 0:
        res = i + n // 5
        print(res)
        break

    n -= 3
    i += 1

    if n == 0:
        print(i)
        break
    elif n < 0:
        print(-1)
        break
