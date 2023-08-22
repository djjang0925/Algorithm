import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
e_students = {i: [0, 0] for i in range(1, 7)}
res = 0

for i in range(n):
    gender, grade = map(int, input().rstrip().split())
    e_students[grade][gender] += 1

for i in e_students:
    for j in e_students[i]:
        res += j // k

        if j % k != 0:
            res += 1

print(res)
