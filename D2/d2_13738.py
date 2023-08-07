test_case = int(input())

for case in range(1, test_case + 1):
    str1 = input()
    str2 = input()

    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]:
            print(f'#{case} 1')
            break
    else:
        print(f'#{case} 0')
