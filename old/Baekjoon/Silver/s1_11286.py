def find_abs():
    if not test_list:
        return 0
    else:
        test_list.get()


test_list = PriorityQueue()
case = int(input())

for i in range(case):
    n = int(input())
    if n == 0:
        print(find_abs())
    elif n < 0:
        test_list.put((1, n))
    else:
        test_list.put(n)
