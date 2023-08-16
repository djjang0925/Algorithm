from collections import deque


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    price = deque(map(int, input().split()))
    sell_point = max(price)
    profit = 0

    for i in range(n):
        now = price.popleft()
        if now < sell_point:
            profit += sell_point - now
        else:
            if not price:
                pass
            else:
                sell_point = max(price)

    print(f'#{case} {profit}')
