def transform(x):
    if x.isdigit():
        x = int(x)
    else:
        x = ord(x) - 55

    temp = []
    while x > 0:
        temp.append(x % 2)
        x //= 2

    temp.reverse()

    while len(temp) != 4:
        temp.insert(0, 0)

    print(''.join(list(map(str, temp))), end='')


test_case = int(input())

for case in range(1, test_case + 1):
    n, h = input().split()

    print(f'#{case}', end=' ')
    for i in h:
        transform(i)
    print()
