test_case = int(input())

i = 1
while i <= test_case:
    a, b = map(int, input().split())
    print(f'#{i} {a // b} {a % b}')
    i += 1