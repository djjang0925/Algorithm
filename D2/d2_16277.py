from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    test_list = list(map(int, input().split()))

    # 카운트 정렬
    count = [0] * (max(test_list) + 1)
    sorted_list = deque([0] * n)

    for num in test_list:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in test_list:
        sorted_list[count[num] - 1] = num
        count[num] -= 1

    # 출력
    print(f'#{case}', end=' ')

    i = 0
    while i < 5:
        print(sorted_list.pop(), end=' ')

        if not sorted_list:
            break

        print(sorted_list.popleft(), end=' ')
        i += 1
    print('')