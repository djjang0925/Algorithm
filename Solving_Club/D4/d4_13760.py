from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    stick = deque(input())
    cnt = 0
    res = 0

    while stick:
        if stick[0] == '(' and stick[1] == ')':
            res += cnt
            stick.popleft()
            stick.popleft()
        elif stick[0] == '(':
            cnt += 1
            stick.popleft()
        elif stick[0] == ')':
            cnt -= 1
            res += 1
            stick.popleft()

    print(f'#{case} {res}')
