from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    t_deque = deque(sorted(list(map(int, input().split()))))
    res = []

    while len(res) != 10:
        res.append(t_deque.pop())
        res.append(t_deque.popleft())

    print(f'#{case}', *res)
