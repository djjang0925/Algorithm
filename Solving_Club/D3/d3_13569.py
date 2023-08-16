test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = list(map(int, input().split()))
    res = 0

    for i in range(n):
        temp = n - 1 - i
        for j in range(i + 1, n):
            box = test_list[i]

            if box <= test_list[j]:
                temp -= 1
            
        if temp > res:
            res = temp

    print(f'#{case} {res}')
