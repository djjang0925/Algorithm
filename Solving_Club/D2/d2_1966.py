test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = list(map(int, input().split()))
    max_index = max(test_list) + 1
    count = {num: 0 for num in range(max_index)}
    res = [0] * len(test_list)

    for num in test_list:
        count[num] += 1

    for num in range(1, max_index):
        count[num] += count[num - 1]

    for num in test_list:
        res[count[num] - 1] = num
        count[num] -= 1

    print(f'#{case}', end=' ')
    print(*res)
