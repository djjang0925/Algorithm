def recursion(level):
    if level == m:
        print(*res)
        return

    for num in test_list:
        if visited[num] == 1:
            continue

        res[level] = num
        visited[num] += 1
        recursion(level + 1)
        visited[num] -= 1


n, m = map(int, input().split())
test_list = [i for i in range(1, n + 1)]
visited = {i: 0 for i in test_list}
res = [0] * m
recursion(0)
