test_case = int(input())

for case in range(1, test_case + 1):
    str1, str2 = input().split()
    cnt = 0

    for i in range(len(str1)):
        if str1[i:i+len(str2)] == str2:
            cnt += 1

    res = len(str1) - len(str2) * cnt + cnt

    print(f'#{case} {res}')
