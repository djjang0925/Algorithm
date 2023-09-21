def recursion(count, num):
    global res

    if num >= b:
        if num == b and count < res:
            res = count
        return

    recursion(count + 1, num * 2)
    recursion(count + 1, int(str(num) + '1'))


a, b = map(int, input().rstrip().split())
res = 21e8

recursion(1, a)

if res == 21e8:
    print(-1)
else:
    print(res)