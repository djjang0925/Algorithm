test_case = int(input())

for case in range(1, test_case + 1):
    n = int(input())
    tree = {i: 0 for i in range(1, n + 1)}

    for i in range(1, n + 1):
        j = 1
        while 1:
            # 부모노드가 비어있으면
            if tree[j] == 0:
                # 좌, 우측 자식노드 확인
                left = j * 2
                right = j * 2 + 1

                if tree[left] == 0:

