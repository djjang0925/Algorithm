test_case = int(input())

for case in range(1, test_case + 1):
    n, k = map(int, input().split())
    puzzle = []
    res = 0

    for i in range(n):
        puzzle.append(list(map(int, input().split())))

    for i in range(n):
        r_count = 0
        c_count = 0
        
        for j in range(n):
            if puzzle[j][i] == 1:
                c_count += 1
            else:
                if c_count == k:
                    res += 1
                c_count = 0

            if puzzle[i][j] == 1:
                r_count += 1
            else:
                if r_count == k:
                    res += 1
                r_count = 0

        if r_count == k:
            res += 1
        
        if c_count == k:
            res += 1

    print(f'#{case} {res}')