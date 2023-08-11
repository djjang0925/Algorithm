# 카운팅 정렬

# n = int(input())
# test_list = []


# for i in range(n):
#     test_list.append(int(input()))
#
# count = [0] * (max(test_list) + 1)
# res = [0] * len(test_list)
#
# for num in test_list:
#     count[num] += 1
#
# for i in range(1, len(count)):
#     count[i] += count[i - 1]
#
# for num in test_list:
#     res[count[num] - 1] = num
#     count[num] -= 1
#
# for num in res:
#     print(num)



# n = int(input())
# test_list = [int(input())]
#
# for i in range(n - 1):
#     num = int(input())
#
#     for j in range(len(test_list)):
#         if num > test_list[j]:
#             continue
#         else:
#             test_list.insert(j, num)
#             break
#     else:
#         test_list.append(num)
#
# for i in range(n):
#     print(test_list[i])


