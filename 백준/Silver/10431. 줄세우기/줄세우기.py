from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

for case in range(1, test_case + 1):
    line = deque(map(int, input().rstrip().split()))
    line.popleft()
    sort = deque()
    res = 0

    while line:
        n = line.popleft()

        if not sort:
            sort.append(n)
        else:
            for i in range(len(sort)):
                if sort[i] > n:
                    res += len(sort) - i
                    sort.insert(i, n)
                    break
            else:
                sort.append(n)

    print(case, res)
