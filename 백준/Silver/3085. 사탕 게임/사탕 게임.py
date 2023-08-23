def count(graph):
    global res

    for i in range(n):
        row = list(graph[i][:])

        cnt = 0
        last = ''
        while row:
            m = row.pop()

            if cnt == 0:
                last = m
                cnt += 1
            else:
                if last == m:
                    cnt += 1
                else:
                    if cnt > res:
                        res = cnt

                    last = m
                    cnt = 1

        if cnt > res:
            res = cnt

    for i in range(n):
        col = list(list(zip(*graph))[i])
        cnt = 0
        last = ''
        while col:
            m = col.pop()

            if cnt == 0:
                last = m
                cnt += 1
            else:
                if last == m:
                    cnt += 1
                else:
                    if cnt > res:
                        res = cnt

                    last = m
                    cnt = 1

        if cnt > res:
            res = cnt


n = int(input())
candies = [list(input()) for _ in range(n)]
candies_r = list(map(list, zip(*candies[::-1])))
res = 0

for i in range(n):
    for j in range(n - 1):
        if candies[i][j] != candies[i][j+1]:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            count(candies)
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

        if candies_r[i][j] != candies_r[i][j+1]:
            candies_r[i][j], candies_r[i][j+1] = candies_r[i][j+1], candies_r[i][j]
            count(candies_r)
            candies_r[i][j], candies_r[i][j+1] = candies_r[i][j+1], candies_r[i][j]

print(res)
