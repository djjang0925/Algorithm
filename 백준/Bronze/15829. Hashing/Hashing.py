l = int(input())
arr = list(input())
res = 0

for i in range(l):
    res += (ord(arr[i]) - 96) * 31 ** i

print(res)