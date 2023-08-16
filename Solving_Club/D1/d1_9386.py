test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    t_list = list(map(int, input()))
    cnt = 0
    max_cnt = 0

    for num in t_list:
        if num == 1:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0
            else:
                cnt = 0
    else:
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{case} {max_cnt}')