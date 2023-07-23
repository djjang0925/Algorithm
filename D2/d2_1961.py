def make(x):
    global num

    for i in range(len(x)):
        temp = ''
        for j in range(len(x[i])):
            temp += str(x[i][j])
    
        res[i][num] = temp

    num += 1



test_case = int(input())

for case in range(1, test_case + 1):
    size = int(input())
    res = [[''] * 3 for _ in range(size)]
    lst = []
    global num
    num = 0

    for i in range(size):
        lst.append(list(map(int, input().split())))

    lst_90 = list(map(list, zip(*lst[::-1])))
    lst_180 = list(map(list, zip(*lst_90[::-1])))
    lst_270 = list(map(list, zip(*lst_180[::-1])))

    make(lst_90)
    make(lst_180)
    make(lst_270)

    print(f'#{case}')

    for i in range(len(res)):
        print(*res[i])
