test_case = int(input())

for case in range(1, test_case + 1):
    str1 = input()

    print(f'#{case}', end=' ')

    for i in range(len(str1) - 1, -1, -1):
        if str1[i] == 'b':
            print('d', end='')
        elif str1[i] == 'd':
            print('b', end='')
        elif str1[i] == 'p':
            print('q', end='')
        elif str1[i] == 'q':
            print('p', end='')

    print('')