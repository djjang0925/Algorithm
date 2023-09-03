for case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    freight = sorted(list(map(int, input().split())), key=lambda x: x)
    trucks = sorted(list(map(int, input().split())), key=lambda x: x)
    res = 0

    while trucks:
        t = trucks.pop()

        while freight:
            f = freight.pop()

            if t >= f:
                res += f
                break

    print(f'#{case} {res}')
