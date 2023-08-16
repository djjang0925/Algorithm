test_case = int(input())

for case in range(1, test_case + 1):
    students = int(input())
    team = students // 3

    print(f'#{case} {team}')