test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    test_list = [list(input()) for _ in range(n)]
    test_list1 = list(map(list, zip(*test_list[::-1])))
    r = m // 2
    flag = False
    res = ''

    for i in range(n):
        for j in range(n - m + 1):
            if m % 2 == 0:
                if test_list[i][j:j+r] == test_list[i][j+r:j+m][::-1]:
                    res = test_list[i][j:j+m]
                    flag = True
                    break
                elif test_list1[i][j:j+r] == test_list1[i][j+r:j+m][::-1]:
                    res = test_list1[i][j:j+m]
                    flag = True
                    break
            else:
                if test_list[i][j:j+r] == test_list[i][j+r+1:j+m][::-1]:
                    res = test_list[i][j:j+m]
                    flag = True
                    break
                elif test_list1[i][j:j+r] == test_list1[i][j+r+1:j+m][::-1]:
                    res = test_list1[i][j:j+m]
                    flag = True
                    break
        if flag is True:
            break

    print(f'#{case}', ''.join(res))
