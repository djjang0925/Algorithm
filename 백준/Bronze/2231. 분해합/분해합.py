import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    x = i
    temp = i
    while 1:
        x += temp % 10

        if temp // 10 == 0:
            break

        temp //= 10

    if x == n:
        print(i)
        break

else:
    print(0)
