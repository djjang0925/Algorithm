def route():
    stack = [s]
    visited = []

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack.extend(graph_dict[n])

    if g not in visited:
        print(f'#{case} 0')
    else:
        print(f'#{case} 1')


test_case = int(input())

for case in range(1, test_case + 1):
    v, e = map(int, input().split())
    graph_dict = {i: [] for i in range(1, v + 1)}

    for i in range(e):
        n1, n2 = map(int, input().split())
        graph_dict[n1].append(n2)

    s, g = map(int, input().split())

    route()
