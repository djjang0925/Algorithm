import sys
input = sys.stdin.readline

arr0 = [1] + [0] * 40
arr1 = [0, 1] + [0] * 39

for i in range(2, 41):
    for j in range(i - 2, i):
        arr0[i] += arr0[j]
        arr1[i] += arr1[j]

t = int(input())

for i in range(t):
    num = int(input())

    print(arr0[num], arr1[num])