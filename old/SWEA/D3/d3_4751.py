from collections import deque


def recursion(level, start, interval):
    if level == 2:
        for i in range(start, n, interval):
            test_list[level][i] = '#'
        for i in range(2, n, 4):
            test_list[level][i] = test_string.popleft()
        return

    for i in range(start, n, interval):
        test_list[level][i] = '#'
        test_list[level + interval][i] = '#'

    if level % 2 == 0:
        j = 2
    else:
        j = 4

    recursion(level + 1, start - 1, j)


test_case = int(input())

for case in range(1, test_case + 1):
    test_string = deque(input())
    n = 5 + (len(test_string) - 1) * 4
    test_list = [['.'] * n for _ in range(5)]

    recursion(0, 2, 4)

    for _ in test_list:
        print(''.join(_))
