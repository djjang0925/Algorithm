# test_case = int(input())
#
# for case in range(1, test_case + 1):
#     day = int(input())
#     prices = list(map(int, input().split()))
#     money = 0
#
#     for i in range(day):
#         s_price = max(prices)                 # max함수를 사용시 메모리를 많이 사용!!
#         if prices[0] < s_price:
#             money += s_price - prices.pop(0)
#         else:
#             prices.pop(0)
#
#     print(f'#{case} {money}')

test_case = int(input())

for case in range(1, test_case + 1):
    day = int(input())
    prices = list(map(int, input().split()))
    money = 0
    max_price = prices[-1]

    for i in range(day - 1, -1, -1):            # max함수가 메모리를 많이 소모 하므로 for문으로 필요한 값만 뽑아서 사용
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            money += max_price - prices[i]

    print(f'#{case} {money}')