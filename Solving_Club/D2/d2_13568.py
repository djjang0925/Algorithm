def sum_list(x, y):
    t_max = 0
    t_min = 1000000
    last_index = x - y + 1

    for i in range(last_index):
        temp = list(test_list[i:i+y])
        if sum(temp) > t_max:
            t_max = sum(temp)
        if sum(temp) < t_min:
            t_min = sum(temp)
    
    # print('max: ',t_max)
    # print('min: ',t_min)
    
    return t_max - t_min



test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    test_list = list(map(int, input().split()))

    print(f'#{case} {sum_list(n, m)}')