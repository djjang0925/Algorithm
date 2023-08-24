n = int(input())
test_site = list(map(int, input().split()))
b, c = map(int, input().split())
res = 0

for i in test_site:
    temp = i - b
    res += 1

    if temp > 0:
        res += temp // c

        if temp % c != 0:
            res += 1

print(res)
