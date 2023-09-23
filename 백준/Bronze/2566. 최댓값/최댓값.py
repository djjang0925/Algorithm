numbers = [list(map(int, input().split())) for _ in range(9)]
res = [0, 0, 0]

for i in range(9):
    for j in range(9):
        if numbers[i][j] > res[0]:
            res = [numbers[i][j], i, j]

print(res[0])
print(res[1] + 1, res[2] + 1)