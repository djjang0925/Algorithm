from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    for i in range(m):
        q.append(q.popleft())

    print(f'#{case} {q[0]}')
