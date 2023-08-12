import sys
input = sys.stdin.readline

test_case = int(input())
test_list = [int(input()) for _ in range(test_case)]

stack = [test_list.pop()]

for i in range(len(test_list)-1, -1, -1):
    if test_list[i] > stack[-1]:
        stack.append(test_list[i])

print(len(stack))
