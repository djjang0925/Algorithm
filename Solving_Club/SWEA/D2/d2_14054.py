from collections import deque

test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    cheese = [(cheese[i], i + 1) for i in range(m)]
    pizza = deque(cheese[:n])
    others = deque(cheese[n:])

    while len(pizza) != 1:
        c = pizza.popleft()

        if c[0] // 2 == 0:
            if others:
                pizza.appendleft(others.popleft())
        else:
            pizza.append((c[0] // 2, c[1]))

    print(f'#{case} {pizza[0][1]}')
