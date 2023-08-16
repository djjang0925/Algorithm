def count_card(x):
    for card in x:
        cards[int(card)] += 1

    max_card = 0
    max_count = 0

    for i in range(10):
        if cards[i] >= max_count:
            max_count = cards[i]
            max_card = i

    # max_card = cards.index(max(cards))
    # max_count = max(cards)
    res = [max_card, max_count]
    
    return res


test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    cards = [0] * 10
    test_list = list(input()[:])

    res = count_card(test_list)

    print(f'#{case} {res[0]} {res[1]}')
