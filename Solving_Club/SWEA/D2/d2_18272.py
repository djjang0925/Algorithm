test_case = int(input())

for case in range(1, test_case + 1):
    stack = []
    test_list = ['(', '{']
    test_list1 = [')', '}']
    test_str = list(input())

    for char in test_str:
        if char in test_list:
            stack.append(char)
        elif char in test_list1:
            if not stack:
                print(f'#{case} 0')
                break
            else:
                n = stack.pop()
                if n == test_list[0] and char != test_list1[0]:
                    print(f'#{case} 0')
                    break
                elif n == test_list[1] and char != test_list1[1]:
                    print(f'#{case} 0')
                    break
    else:
        if not stack:
            print(f'#{case} 1')
        else:
            print(f'#{case} 0')
