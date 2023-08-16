def find_x(total, find):
    count = 0
    l, r = 1, total
    c = int((l + r)/2)

    if c == find:
        return 0

    while c != find:
        if c - find < 0:
            l = c
        else:
            r = c

        c = int((l + r) / 2)
        count += 1

    return count


test_case = int(input())

for case in range(1, test_case + 1):
    p, a, b = map(int, input().split())

    a_count = find_x(p, a)
    b_count = find_x(p, b)

    if a_count > b_count:
        print(f'#{case} B')
    elif a_count == b_count:
        print(f'#{case} 0')
    else:
        print(f'#{case} A')