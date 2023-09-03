# 우석 1
# w1, w2 = [input() for _ in range(2)]
# a1 = {chr(i): 0 for i in range(97, 123)}
# a2 = {chr(i): 0 for i in range(97, 123)}
#
# for i in range(len(w1)):
#     a1[w1[i]] += 1
#     a2[w2[i]] += 1
#
# if a1 == a2:
#     print('애너그램 맞음')
# else:
#     print('애너그램 아님')
#
# 우석 2
# w1, w2 = [input() for _ in range(2)]
# a1 = {chr(i): 0 for i in range(97, 123)}
# a2 = {chr(i): 0 for i in range(97, 123)}
# res = 0
#
# for i in w1:
#     a1[i] += 1
#
# for i in w2:
#     a2[i] += 1
#
# for i in a1:
#     if a1[i] != a2[i]:
#         res += abs(a1[i] - a2[i])
#
# print(f'{res}개')
#
# 우석 3
# from itertools import permutations
#
# w1, w2 = [(list(input())) for _ in range(2)]
#
# c1 = set(permutations(w1, len(w1)))
# res = 0
#
#
# for j in range(len(w2) - len(w1) + 1):
#     c2 = tuple(w2[j:j+len(w1)])
#     for i in c1:
#         if i == c2:
#             res += 1
#
# print(f'{res}개')
