test_case = int(input())

for case in range(1, test_case + 1):
    a, b = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    res = 0
    
    if a > b:
        for i in range(a - b + 1):
            temp = 0
        
            for j in range(len(lst2)):
                temp += lst2[j] * lst1[j + i]

            if res < temp:
                res = temp
    
    elif a < b:
        for i in range(b - a + 1):
            temp = 0

            for j in range(len(lst1)):
                temp += lst1[j] * lst2[j + i]

            if res < temp:
                res = temp
    
    else:
        for i in range(len(lst1)):
            res += lst1[i] * lst2[i]

    print(f'#{case} {res}')
