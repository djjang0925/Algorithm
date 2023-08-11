def dfs():
    stack = [0]

    while stack:
        n = stack.pop()
        if n == 99:
            return 1

        if visited[n] == 0:
            visited[n] = 1
            stack.extend(route[n])

    return 0


for case in range(10):
    c, m = map(int, input().split())
    test_list = list(map(int, input().split()))
    route = {i: [] for i in test_list}
    visited = {i: 0 for i in test_list}

    for i in range(0, m*2, 2):
        route[test_list[i]].append(test_list[i+1])

    print(f'#{c} {dfs()}')
