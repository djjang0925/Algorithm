test_case = int(input())

for case in range(1, test_case + 1):
    print(f'#{case}')

    t_case = int(input())
    paper = []

    for i in range(t_case):
        tc = list(input().split())

        for j in range(int(tc[1])):
            paper.append(tc[0])

    k = 1
    while k < len(paper) + 1:
        print(paper[k - 1], end='')
        if k % 10 == 0:
            print('')
        k += 1
    
    print('')
