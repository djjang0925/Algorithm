test_case = int(input())

for i in range(test_case):
    n = int(input())
    students = list(map(int, input().split()))
    idx = [0] * 101
    res = 0

    for j in range(len(students)):
        idx[students[j]] += 1

        if idx[students[j]] >= idx[res]:
            res = students[j]

    print(f'#{n} {res}')


# test_case = int(input())
#
# for i in range(test_case):
#     n = int(input())
#     students = list(map(int, input().split()))
#     students.sort()
#     s = set(students)
#     res = 0
#     ans = 0
#
#     for j in s:
#         temp = students.count(j)
#         if temp >= res:
#             res = temp
#             ans = j
#
#     print(f'#{n} {ans}')
