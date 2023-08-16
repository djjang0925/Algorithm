# test_case = int(input())
#
# for case in range(1, test_case + 1):
#     n = int(input())
#     triangle = []
#
#     for i in range(n):
#         triangle.append([1]*(i + 1))
#
#     for i in range(n):
#         # print(f'길이: {len(triangle[i])}')
#         if len(triangle[i]) <= 2:
#             continue
#         else:
#             for j in range(1, len(triangle[i]) - 1):
#                 triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
#
#     print(f'#{case}')
#     for i in range(n):
#         print(*triangle[i])

def tri(n):
    if n > 1:
        return n * tri(n - 1)
    else:
        return 1


test_case = int(input())

for case in range(1, test_case + 1):
    num = int(input())
    triangle = []

    for i in range(num):
        temp = []

        for j in range(i + 1):
            number = tri(i) // (tri(i-j) * tri(j))
            temp.append(number)

        triangle.append(temp)

    print(f'#{case}')
    for i in range(num):
        print(*triangle[i])
