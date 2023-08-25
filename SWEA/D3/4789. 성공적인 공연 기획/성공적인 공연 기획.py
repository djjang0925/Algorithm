test_case = int(input())

for case in range(1, test_case + 1):
    audiences = list(map(int, input()))
    clap = 0
    res = 0

    for i in range(len(audiences)):
        if audiences[i] == 0:
            continue

        if i <= clap:
            clap += audiences[i]
        else:
            hire = i - clap
            clap += hire + audiences[i]
            res += hire

    print(f'#{case} {res}')
