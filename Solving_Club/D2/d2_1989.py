test_case = int(input())

for case in range(1, test_case + 1):
    input_string = input()
    palindrome = input_string[::-1]

    if palindrome == input_string:
        res = 1
    else:
        res = 0

    print(f'#{case} {res}')
