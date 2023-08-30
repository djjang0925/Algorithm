import sys
input = sys.stdin.readline


def find(x, y):
    while y:
        t = x
        x = y
        y = t % y

    return x


n, m = map(int, input().rstrip().split())
mul = m//n
temp = []
if n == m:
    print(n, m)
else:
    for i in range(1, mul):
        if mul % i == 0:
            j = mul // i

            if find(i, j) == 1:
                temp.append([i, mul//i])

    ans = []
    ans_temp = 21e8
    for i in temp:
        if sum(i) < ans_temp:
            ans = i
            ans_temp = sum(i)

    print(ans[0] * n, ans[1] * n)
