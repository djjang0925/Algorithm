import heapq

n = int(input())
cards = []
ans = 0

for i in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    ans += temp
    heapq.heappush(cards, temp)

print(ans)