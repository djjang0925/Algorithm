lst = list(input())

for i in range(len(lst)):
    if (ord(lst[i]) >= ord('a')) and (ord(lst[i]) <= ord('z')):
        lst[i] = chr(ord(lst[i]) - 32)

for i in range(len(lst)):
    print(lst[i], end = '')
