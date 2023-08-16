import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
cable = [int(input()) for _ in range(k)]
short, long = 1, max(cable)

while short <= long:
    cnt = 0
    mid = (short + long) // 2

    for lan in cable:
        cnt += lan // mid

    if cnt < n:
        long = mid - 1
    else:
        short = mid + 1

print(long)
