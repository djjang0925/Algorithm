test_list = list(map(int, input()))
count = [0] * (max(test_list) + 1)

temp = 0

for num in test_list:
    if num == 6 or num == 9:
        temp += 1
    else:
        count[num] += 1

max_num = max(count)

if temp % 2 == 0:
    temp //= 2
else:
    temp = temp // 2 + 1

if max_num >= temp:
    print(max_num)
else:
    print(temp)
