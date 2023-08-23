import sys
input = sys.stdin.readline

n = int(input())
graph = dict()
height = []
start, end = 21e8, 0
res = 0
cnt = 0
last = 0

for i in range(n):
    l, h = map(int, input().rstrip().split())
    height.append(h)
    graph[l] = h

    if l < start:
        start = l
    if l > end:
        end = l

height.sort()

for i in range(start, end + 1):
    if i in graph:
        if graph[i] == height[-1]:
            res += height.pop()
            start = i + 1
            break
        else:
            if graph[i] < last:
                res += last
            else:
                res += graph[i]
                last = graph[i]

            height.remove(graph[i])
    else:
        res += last

if start <= end:
    for i in range(start, end + 1):
        if i in graph:
            if graph[i] == height[-1]:
                res += height.pop() * (cnt + 1)
                cnt = 0
            else:
                cnt += 1
                height.remove(graph[i])
        else:
            cnt += 1

print(res)
