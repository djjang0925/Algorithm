test_case = int(input())

for case in range(1, test_case + 1):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    students = []

    for i in range(n):
        student = list(map(int, input().split()))   # 학생 성적 입력
        total = student[0] * 0.35 + student[1] * 0.45 + student[2] * 0.2    # 총점 계산
        students.append(total)      # 학생들 정보에 등록

    student_k = students[k - 1]     # k번째 학생 성적
    students.sort(reverse=True)     # 내림차순 정렬

    if n > 10:
        temp = students.index(student_k) // (n // 10)
        res = grade[temp]
    else:
        res = grade[students.index(student_k)]      # 성적 할당

    print(f'#{case} {res}')