t = int(input())
apt = [[i for i in range(15)]]

for i in range(1, 15):
    temp = [0]
    for j in range(1, 15):
        x = temp[j-1] + apt[i-1][j]
        temp.append(x)
    apt.append(temp)

for i in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])
