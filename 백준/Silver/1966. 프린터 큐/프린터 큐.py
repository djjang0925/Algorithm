from collections import deque

test_case = int(input())

for case in range(test_case):
    n, p = map(int, input().split())
    priority = list(map(int, input().split()))
    papers = deque([[priority[i], i] for i in range(n)])
    res = 0

    while 1:
        x = papers.popleft()

        if x[0] < max(priority):
            papers.append(x)
        else:
            priority.remove(x[0])
            res += 1

            if x[1] == p:
                break

    print(res)
