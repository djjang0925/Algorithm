# test_case = int(input())
#
# for i in range(test_case):
#     n = int(input())
#     list_n = list(map(int, input().split()))    # 돌이 떨어진 위치 리스트
#     res = 100_000                               # 최댓 값을 1등으로 지정
#     cnt = 0                                     # 동일한 결과 값을 낸 사람
#
#     for j in range(len(list_n)):
#         if abs(list_n[j]) < res:                # 위치 리스트와 결과 값 비교
#             res = abs(list_n[j])                # 값 재할당
#             cnt = list_n.count(res)             # 동일한 거리 값 카운트
#             cnt += list_n.count(-res)
#
#     print(f'#{i + 1} {res} {cnt}')

test_case = int(input())

for j in range(test_case):
    n = int(input())
    list_n = list(map(int, input().split()))    # 돌이 떨어진 위치 리스트

    for i in range(len(list_n)):                # 배열을 절대 값으로 재할당
        list_n[i] = abs(list_n[i])

    res = min(list_n)                           # 최소 값
    cnt = list_n.count(res)                     # 동일 거리

    print(f'#{test_case} {res} {cnt}')
