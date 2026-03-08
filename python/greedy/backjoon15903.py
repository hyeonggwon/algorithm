import heapq

N, M = map(int, input().split())
numq = list(map(int, input().split()))

heapq.heapify(numq)

for _ in range(M):
    a, b = heapq.heappop(numq), heapq.heappop(numq)
    heapq.heappush(numq, a + b)
    heapq.heappush(numq, a + b)

print(sum(numq))