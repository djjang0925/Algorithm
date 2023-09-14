import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().rstrip().split())) for _ in range(n)]
rating = {i: 0 for i in range(n)}

for i in range(n):
    cnt = 1

    for j in range(n):
        if i == j:
            continue

        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1

    rating[i] = cnt

for i in range(n):
    print(rating[i], end=' ')