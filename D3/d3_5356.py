test_case = int(input())

for case in range(1, test_case + 1):
    test_list = [input() for i in range(5)]

    print(f'#{case}', end=' ')

    for i in range(15):
        for word in test_list:
            try:
                print(word[i], end='')
            except IndexError:
                continue
    print('')
