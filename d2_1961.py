test_case = int(input())

for case in range(1, test_case + 1):
    size = int(input())
    lst = [[0] * size for _ in range(size)]
    res = [[''] * 3 for _ in range(size)]

    num = 1
    for i in range(size):
        for j in range(size):
            lst[i][j] = num
            num += 1

    lst_90 = list(map(list, zip(*lst[::-1])))

    temp = ''
    for i in range(len(lst_90)):
        for j in range(len(lst_90[i])):
            

    