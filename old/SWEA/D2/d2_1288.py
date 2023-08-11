def counting(x):
    while x > 0:
        lst[x % 10] += 1
        x //= 10


def check(x):
    for j in range(len(x)):
        if x[j] == 0:
            return False
    else:
        return True


test_case = int(input())

for case in range(test_case):
    sheep = int(input())
    lst = [0] * 10

    i = 1
    while check(lst) == False:
        temp = sheep * i
        counting(temp)
        check(lst)
        i += 1

    print(f'#{case + 1} {temp}')
