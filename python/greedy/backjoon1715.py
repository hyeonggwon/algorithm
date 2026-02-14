import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = [int(input()) for _ in range(n)]
heapq.heapify(q)

result = 0
while len(q) >= 2:
    sum = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, sum)
    result += sum

print(result)