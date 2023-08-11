import sys
input = sys.stdin.readline

n = int(input())
test_list = list(map(int, input().rstrip().split()))
stack = []
res = [0] * n

for i in range(n):
    s = test_list[i]

    while stack:
        if s > stack[-1][0]:
            stack.pop()
        else:
            res[i] = stack[-1][1]
            break

    stack.append([s, i + 1])

print(*res)
