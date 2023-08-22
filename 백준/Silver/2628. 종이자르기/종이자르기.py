x, y = map(int, input().split())
n = int(input())
cut = [list(map(int, input().split())) for _ in range(n)]
cut_r = [0, y]
cut_c = [0, x]
x, y = 0, 0

for i in cut:
    if i[0] == 1:
        cut_c.append(i[1])
    else:
        cut_r.append(i[1])

cut_c.sort()
cut_r.sort()

for i in range(0, len(cut_r) - 1):
    if y < cut_r[i+1] - cut_r[i]:
        y = cut_r[i+1] - cut_r[i]

for i in range(0, len(cut_c) - 1):
    if x < cut_c[i+1] - cut_c[i]:
        x = cut_c[i+1] - cut_c[i]

print(x*y)
