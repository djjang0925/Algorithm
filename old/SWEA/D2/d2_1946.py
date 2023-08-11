test_case = int(input())

for case in range(1, test_case + 1):
    cnt = 0
    n = int(input())
    test_list = [list(input().split()) for _ in range(n)]

    print(f'#{case}')

    for _ in test_list:
        for i in range(int(_[1])):
           print(_[0], end='')
           cnt += 1

           if cnt == 10:
               cnt = 0
               print('')

    print('')
