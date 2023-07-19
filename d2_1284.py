def com_a(x, y):
    return x * y            # 리터랑 요금제


def com_b(a, b, c, d):
    if a <= b:
        return c            # b리터 이하로 사용시 기본 요금
    else:
        return c + (a - b) * d    # b리터 초과로 사용시 추가 요금


test_case = int(input())

for i in range(test_case):
    p, q, r, s, w = map(int, input().split())
    res = min(com_a(w, p), com_b(w, r, q, s))
    print(f'#{i + 1} {res}')
