test_case = int(input())

for case in range(1, test_case + 1):
    num = int(input())
    temp = num // 2
    num1, num2 = 0, 0
    
    for i in range(2, temp):
        if temp % i == 0:
            num1 = temp
        else:
            break
        
    
    num2 = num - num1

    print(num1, num2)









# 4   2 2
# 6   3 3
# 8   3 5
# 10  5 5
# 12  5 7
# 14  7 7
# 16  5 11
# 18  7 11
# 20  7 13
# 22  11 11
# 24  11 13
# 26  13 13