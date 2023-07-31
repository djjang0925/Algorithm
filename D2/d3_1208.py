test_case = 11

for case in range(1, test_case):
    dump = int(input())
    box = list(map(int, input().split()))

    i = 0
    while i < dump:
        index_max = box.index(max(box))
        index_min = box.index(min(box))

        box[index_max] -= 1
        box[index_min] += 1

        i += 1

    res = max(box) - min(box)
    print(f'#{case} {res}')
