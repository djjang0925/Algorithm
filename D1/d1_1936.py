a, b = map(int, input().split())
sic, rck, pap = 1, 2, 3
res = a - b

def game(x):
    if x == -2:
        print('A')
    elif x == 2:
        print('B')
    elif x > 0:
        print('A')
    else:
        print('B')

game(res)