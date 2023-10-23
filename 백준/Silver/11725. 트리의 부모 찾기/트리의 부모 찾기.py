from collections import deque

import sys
input = sys.stdin.readline


def find(tree):
    q = deque([1])

    while q:
        cur = q.popleft()

        for i in tree[cur]:
            if res[i] == 0 and i != 1:
                res[i] = cur
                q.append(i)


n = int(input())

graph = {i: [] for i in range(1, n+1)}
res = {i: 0 for i in range(1, n+1)}

for i in range(n-1):
    a, b = map(int, input().split())
    
    # 트리의 루트 노드가 1번 이라고 주어 졌기 때문에 양방향 그래프로 입력 받더라도 위에서 부터 아래 방향으로 그래프를 순회한다.
    graph[a].append(b)
    graph[b].append(a)

find(graph)

for i in range(2, n + 1):
    print(res[i])