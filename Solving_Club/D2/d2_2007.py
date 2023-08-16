test_case = int(input())

for case in range(1, test_case + 1):
    c_input = input()
    count = 0

    for i in range(1, 16):
        if c_input[:i] == c_input[i:2*i]:
            print(f'#{case} {i}')
            break
