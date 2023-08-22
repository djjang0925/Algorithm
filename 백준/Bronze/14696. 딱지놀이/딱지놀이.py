import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ddakji = {i: [0, 0, 0, 0, 0] for i in [1, 2]}

    for j in range(1, 3):
        temp = list(map(int, input().rstrip().split()))

        for k in range(1, len(temp)):
            ddakji[j][temp[k]] += 1

    for i in range(4, 0, -1):
        if ddakji[1][i] == ddakji[2][i]:
            continue
        elif ddakji[1][i] > ddakji[2][i]:
            print('A')
            break
        else:
            print('B')
            break
    else:
        print('D')
