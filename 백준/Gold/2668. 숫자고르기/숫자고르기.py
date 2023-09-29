def find(x):
    stack = [x]
    visited = {i: 0 for i in range(1, n + 1)}
    v2 = {i: 0 for i in range(1, n + 1)}
    visited[x] = 1

    while stack:
        now = stack.pop()
        v2[graph[now]] = 1

        if visited[graph[now]] == 0:
            visited[graph[now]] = 1
            stack.append(graph[now])

    temp = []
    for i in range(1, n + 1):
        if visited[i] == v2[i] == 1:
            temp.append(i)
        elif visited[i] != v2[i]:
            return []

    return temp


n = int(input())
graph = {i: 0 for i in range(1, n + 1)}

for i in range(1, n + 1):
    graph[i] = int(input())

res = []
same = []
for i in range(1, n + 1):
    if i == graph[i]:
        same.append(i)
        continue

    res.extend(find(i))

res.extend(same)
res = list(set(res))
res.sort()

print(len(res))
for i in res:
    print(i)