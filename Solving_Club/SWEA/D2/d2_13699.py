test_case = int(input())

for case in range(1, test_case + 1):
    paper = [[0]* 10 for _ in range(10)]
    color = int(input())
    cnt = 0

    for i in range(color):
        paint = list(map(int, input().split()))

        for j in range(paint[0], paint[2] + 1):
            for k in range(paint[1], paint[3] + 1):
                paper[j][k] += paint[-1]

                if paper[j][k] == 3:
                    cnt += 1

    print(f'#{case} {cnt}')