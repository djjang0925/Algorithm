test_case = int(input())

for case in range(1, test_case + 1):
    # 1000000
    money = int(input()) // 10
    change_list = [0] * 8

    i = 0
    while money != 0:
        if i >= 6:
            change_list[i + 1] += money // 5
            change_list[i] = money % 5
            break
            
        else:    
            change = money % 10

            if change >= 5:
                change_list[i + 1] += change // 5
                change_list[i] = change % 5
            else:
                change_list[i] = change
        
        money //= 10
        i += 2

    change_list.reverse()
    print(f'#{case}')
    print(*change_list)
