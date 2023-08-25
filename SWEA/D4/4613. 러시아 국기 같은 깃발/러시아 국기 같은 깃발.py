test_case = int(input())

for case in range(1, test_case + 1):
    n, m = map(int, input().split())
    russia = []
    res = []

    for i in range(n):
        russia.append(list(input()))

    top = russia[0].count('W')
    bottom = russia[-1].count('R')

    # 모든 경우의 수 다 탐색
    w = 0
    for i in range(n - 2):
        w += m - russia[i].count('W')
        b = 0
         
        for j in range(i + 1, n - 1):
            b += m - russia[j].count('B')
            r = 0
            
            for k in range(j + 1, n):
                r += m - russia[k].count('R')
                
            res.append(w + b + r)
    
    print(f'#{case} {min(res)}')
