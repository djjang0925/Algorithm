def messi_gimossi():
    if m < len(messi[-1]) or len(messi[-1]) == m:
        return

    messi[2] = messi[0] + ' ' + messi[1]
    messi[0], messi[1] = messi[1], messi[2]
    messi_gimossi()


def binary_search(x):
    s = 0
    e = len(messi[2]) - 1

    while 1:
        m = (s + e) // 2

        if m > x - 1:
            e = m - 1
        elif m < x - 1:
            s = m + 1
        else:
            return messi[2][m]


messi = ['Messi', 'Messi Gimossi', '']
m = int(input())
messi_gimossi()
res = binary_search(m)
if res == ' ':
    print('Messi Messi Gimossi')
else:
    print(res)
