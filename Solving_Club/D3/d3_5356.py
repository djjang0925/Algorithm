test_case = int(input())

for case in range(1, test_case + 1):
    string = [list(input()) for _ in range(5)]

    print(f'#{case}', end=' ')
    for i in range(15):
        for j in range(5):
            try:
                print(string[j][i], end='')
            except IndexError:
                continue
    print()
