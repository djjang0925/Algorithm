import sys
input = sys.stdin.readline

n, m, b = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
res = [21e8, 0]

for h in range(257):
    use = 0
    get = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= h:
                get += graph[i][j] - h
            else:
                use += h - graph[i][j]
                
    if (b + get) - use >= 0:
        if use + get * 2 <= res[0]:
            res[0] = use + get * 2
            res[1] = h

print(*res)