import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().rstrip().split()))
students = {(i + 1): card[i] for i in range(n)}
temp = []
res = [1]

for i in range(2, n + 1):
    m = students[i]
    temp = res[(i - 1) - m:]
    res = res[:(i - 1) - m]
    res.append(i)
    res.extend(temp)

print(*res)
