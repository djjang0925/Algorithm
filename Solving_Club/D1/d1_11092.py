test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    t_list = list(map(int, input().split()))

    index_max, index_min = 0, 0

    for i in range(1, n):
        if t_list[i] < t_list[index_min]:
            index_min = i

        if t_list[i] >= t_list[index_max]:
            index_max = i

    print(f'#{case} {abs(index_max - index_min)}')
