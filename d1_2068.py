test_case = int(input())

for i in range(test_case):
    lst = list(map(int, input().split()))
    max = 0

    for j in range(len(lst)):
        if max < lst[j]:
            max = lst[j]

    print(f'#{i + 1} {max}')
