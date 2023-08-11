def recursion(level):
    global res
    temp = 0
    for i in range(level):
        temp += path[i] * 10 ** i
    if res < temp <= n:
        res = temp

    if level == stop:
        return

    for num in numbers:
        path[level] = num
        recursion(level + 1)


n, m = map(int, input().split())
stop = len(str(n))
numbers = list(map(int, input().split()))
path = [0] * stop
res = 0

recursion(0)
print(res)
