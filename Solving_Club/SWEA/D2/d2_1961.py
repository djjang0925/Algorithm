test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = [list(input().split()) for _ in range(n)]
    t_list90 = list(map(list, zip(*test_list[::-1])))
    t_list180 = list(map(list, zip(*t_list90[::-1])))
    t_list270 = list(map(list, zip(*t_list180[::-1])))

    print(f'#{case}')

    for i in range(n):
        print(''.join(t_list90[i]), ''.join(t_list180[i]), ''.join(t_list270[i]))
