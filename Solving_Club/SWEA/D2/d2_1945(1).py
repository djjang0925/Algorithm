def factorization(x):
    for key in count_dict:
        while 1:
            if x % key != 0:
                break
            else:
                count_dict[key] += 1
                x //= key


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    count_dict = {i: 0 for i in [2, 3, 5, 7, 11]}

    factorization(n)

    print(f'#{case}', *list(count_dict.values()))
