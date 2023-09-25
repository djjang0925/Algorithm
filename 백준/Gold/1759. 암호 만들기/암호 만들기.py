from itertools import combinations

l, c = map(int, input().split())
arr = sorted(list(input().split()))

comb = list(combinations(arr, l))
gather = ['a', 'e', 'i', 'o', 'u']

for i in comb:
    length = 0

    for j in i:
        if j in gather:
            length += 1

    if length >= 1 and len(i) - length >= 2:
        print(''.join(i))