test_case = int(input())

for case in range(1, test_case + 1):
    str1 = input()
    str2 = input()
    test_dict = {i: 0 for i in str1}

    for alpha in str2:
        if alpha in str1:
            test_dict[alpha] += 1

    print(f'#{case} {max(test_dict.values())}')
