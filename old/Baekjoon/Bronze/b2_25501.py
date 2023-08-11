def isPalindrome(s):
    x = len(s)
    recursion(s, 0, x - 1)

    if flag is False:
        print(1, cnt)
    else:
        print(0, cnt)


def recursion(s, l, r):
    global cnt, flag
    cnt += 1
    if l >= r:
        return
    elif s[l] != s[r]:
        flag = True
        return
    else:
        return recursion(s, l + 1, r - 1)


n = int(input())
for i in range(n):
    cnt = 0
    flag = False
    s = input()
    isPalindrome(s)
