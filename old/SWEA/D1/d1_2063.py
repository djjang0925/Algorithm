test_case = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = test_case // 2

print(lst[res])