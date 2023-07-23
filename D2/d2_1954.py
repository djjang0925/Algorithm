test_case = int(input())

for case in range(1, test_case + 1):
    num = int(input())
    snail = [[0] * num for _ in range(num)]
    count = 1
    do = 0
    if num % 2 == 1:
        do = num // 2 + 1
    else:
        do = num // 2

    for a in range(do):
        for i in range(num):
            if snail[a][i] != 0:
                continue
            
            snail[a][i] = count
            count += 1
        
        else:
            for j in range(num):
                if snail[j][i - a] != 0:
                    continue
                
                snail[j][i - a] = count
                count += 1

            else:
                for k in range(i, -1, -1):
                    if snail[i - a][k] != 0:
                        continue

                    snail[i - a][k] = count
                    count += 1

                else:
                    for l in range(j, 0, -1):
                        if snail[l][a] != 0:
                            continue

                        snail[l][a] = count
                        count += 1

                    
    print(f'#{case}')            
    for i in range(num):
        print(*snail[i])