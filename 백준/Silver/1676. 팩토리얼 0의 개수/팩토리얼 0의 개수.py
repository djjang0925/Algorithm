def factorial(level):
    if level == 1 or level == 0:
        return 1

    return level * factorial(level - 1)


n = int(input())
f = list(map(int, str(factorial(n))))
cnt = 0

while 1:
    x = f.pop()

    if x != 0:
        break

    cnt += 1

print(cnt)
