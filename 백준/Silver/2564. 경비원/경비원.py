import sys
input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
n = int(input())
res = 0
distances = []

for i in range(1, n + 2):
    direction, distance = list(map(int, input().rstrip().split()))
    if direction == 1:
        distances.append(2*y + x + (x - distance))
    elif direction == 2:
        distances.append(y + distance)
    elif direction == 3:
        distances.append(distance)
    elif direction == 4:
        distances.append(y + x + (y - distance))

now = distances.pop()

for i in distances:
    if abs(now - i) > (x+y):
        res += 2 * (x+y) - abs(now - i)
    else:
        res += abs(now - i)

print(res)
