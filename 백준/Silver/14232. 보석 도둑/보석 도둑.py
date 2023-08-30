k = int(input())
res = []

for i in range(2, int(k**0.5) + 1):
    while k % i == 0:
        res.append(i)
        k //= i

if k != 1:
    res.append(k)

print(len(res))
print(*res)
