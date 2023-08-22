n, l = map(int, input().split())
information = [list(map(int, input().split())) for _ in range(n)]
time = 0
now = 0

for i in information:
    time += (i[0] - now)
    now = i[0]

    if 0 <= time % (i[1] + i[2]) < i[1]:
        time += i[1] - (time % (i[1] + i[2]))

print(time + (l - now))
