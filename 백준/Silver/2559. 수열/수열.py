import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
temperatures = list(map(int, input().rstrip().split()))
temp = [sum(temperatures[:k])]

for i in range(k, n):
    temp.append(temp[-1] - temperatures[i - k] + temperatures[i])

print(max(temp))
