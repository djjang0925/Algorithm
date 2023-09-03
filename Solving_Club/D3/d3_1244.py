def change(c):
    global ans

    if c == 0:
        temp = int(''.join(numbers))

        if temp > ans:
            ans = temp
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            try:
                if used[(''.join(numbers), c - 1)]:
                    continue
            except KeyError:
                used[(''.join(numbers), c - 1)] = 0
                change(c - 1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


for case in range(1, int(input()) + 1):
    money, count = map(int, input().split())
    numbers = list(str(money))
    used = dict()
    ans = 0

    change(count)

    print(f'#{case} {ans}')
