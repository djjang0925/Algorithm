import sys
input = sys.stdin.readline


def union(a, b):
    u[a] = b
    d[a] += abs(a - b) % 1000


def find(m):
    if u[m] == 0:
        return m
    
    ret = find(u[m])
    d[m] += d[u[m]]
    u[m] = ret

    return ret


test_case = int(input())

for case in range(test_case):
    n = int(input())
    u = {i: 0 for i in range(1, n + 1)}
    d = {i: 0 for i in range(1, n + 1)}

    while 1:
        command = list(input().rstrip().split())

        if command[0] == 'E':
            find(int(command[1]))
            print(d[int(command[1])])
        elif command[0] == 'I':
            union(int(command[1]), int(command[2]))
        else:
            break
