for case in range(4):
    sx1, sy1, ex1, ey1, sx2, sy2, ex2, ey2 = map(int, input().split())
    res = 'd'

    if sx1 == ex2 or ex1 == sx2:
        if sy1 == ey2 or ey1 == sy2:
            res = 'c'

    if sx1 == ex2 or sx2 == ex1:
        if sy1 <= sy2 < ey1 or sy2 <= sy1 < ey2:
            res = 'b'

    if sy1 == ey2 or sy2 == ey1:
        if sx1 <= sx2 < ex1 or sx2 <= sx1 < ex2:
            res = 'b'

    if sx1 <= sx2 < ex1 or sx2 <= sx1 < ex2:
        if sy1 <= sy2 < ey1 or sy2 <= sy1 < ey2:
            res = 'a'

    print(res)
