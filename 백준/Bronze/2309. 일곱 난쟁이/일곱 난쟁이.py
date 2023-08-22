def recursion(level, total, start):
    global res
    if level == 7:
        if total == 100:
            res = path.copy()
            res.sort()
        return

    for i in range(start, 9):
        path[level] = dwarfs[i]
        recursion(level + 1, total + dwarfs[i], i + 1)


dwarfs = []
path = [0] * 7
res = []
for i in range(9):
    dwarfs.append(int(input()))

recursion(0, 0, 0)

for i in res:
    print(i)
