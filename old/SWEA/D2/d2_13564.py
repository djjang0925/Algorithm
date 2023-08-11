test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = list(map(int, input().split()))
    res = max(test_list) - min(test_list)
    print(f'#{case} {res}')