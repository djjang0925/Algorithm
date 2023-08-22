l = int(input())
n = int(input())
cake = [0] * (l + 1)
expectation = 0
ex_res = 0
peaces = 0
res = 0

for i in range(1, n + 1):
    s, e = map(int, input().split())
    temp = 0

    if (e - s + 1) > expectation:
        expectation = e - s + 1
        ex_res = i

    for j in range(s, e + 1):
        if cake[j] == 0:
            cake[j] = i
            temp += 1

    if temp > peaces:
        peaces = temp
        res = i

print(ex_res)
print(res)
