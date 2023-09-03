def change_2():
    for i in range(len(numbers[0])):
        for j in range(2):
            temp = list(numbers[0])

            if temp[i] != str(j):
                temp[i] = str(j)
                check.append(int(''.join(temp), 2))
                break


def change_3():
    for i in range(len(numbers[1])):
        for j in range(3):
            temp = list(numbers[1])
            if temp[i] != str(j):
                temp[i] = str(j)
                if int(''.join(temp), 3) in check:
                    print(f'#{case}', int(''.join(temp), 3))


for case in range(1, int(input()) + 1):
    numbers = list(input() for _ in range(2))
    check = []

    change_2()
    change_3()
