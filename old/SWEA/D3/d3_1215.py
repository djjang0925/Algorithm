for case in range(1, 11):
    n = int(input())
    test_list = [list(input()) for _ in range(8)]
    test_list1 = list(map(list, zip(*test_list[::-1])))
    cnt = 0
    m = n // 2

    for i in range(8):
        for j in range(8 - n + 1):
            if n % 2 == 0:
                if test_list[i][j:j+m] == test_list[i][j+m:j+n][::-1]:
                    cnt += 1
                if test_list1[i][j:j+m] == test_list1[i][j+m:j+n][::-1]:
                    cnt += 1
            else:
                if test_list[i][j:j+m] == test_list[i][j+m+1:j+n][::-1]:
                    cnt += 1
                if test_list1[i][j:j+m] == test_list1[i][j+m+1:j+n][::-1]:
                    cnt += 1

    print(f'#{case} {cnt}')
