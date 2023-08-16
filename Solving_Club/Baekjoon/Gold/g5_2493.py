import sys
input = sys.stdin.readline

n = int(input())
test_list = list(map(int, input().rstrip().split()))
res = [0] * n
stack = []

for i in range(n):
    while stack:
        if stack[-1][0] > test_list[i]:
            res[i] = stack[-1][1]
            break
        else:
            stack.pop()

    stack.append([test_list[i], i + 1])

print(*res)
