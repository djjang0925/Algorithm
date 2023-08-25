def counselling(start, pay):
    global money

    if counsels[start][0] + start - 1 > n:
        return

    if money < pay:
        money = pay

    for i in range(start + 1, n + 1):
        if i > start + counsels[start][0] - 1:
            counselling(i, pay + counsels[i][1])


n = int(input())
counsels = {i: [] for i in range(1, n + 1)}
money = 0

for i in range(1, n + 1):
    counsels[i] = list(map(int, input().split()))

for i in counsels:
    counselling(i, counsels[i][1])

print(money)
