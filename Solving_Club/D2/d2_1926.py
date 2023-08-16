num = int(input())

for i in range(1, num + 1):
    num = str(i)
    count = 0

    for j in range(len(num)):
        if (num[j] == '3') or (num[j] == '6') or (num[j] == '9'):
            print('-', end='')
            count += 1

    if count > 0:
        print(' ', end = '')

    if count == 0:
        print(i, end=' ')