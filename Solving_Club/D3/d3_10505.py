from functools import reduce

test_case = int(input())

for case in range(1, test_case + 1):
    cnt = 0
    total = int(input())
    people = list(map(int, input().split()))
    avg = reduce(lambda x, y: x + y, people) // total
	
    for person in people:
        if person <= avg:
            cnt += 1

    print(f'#{case} {cnt}')
