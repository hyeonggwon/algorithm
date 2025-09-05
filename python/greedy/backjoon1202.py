import heapq
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
heapq.heapify(jewel)

backpack = []
for _ in range(k):
    backpack.append(int(input()))
backpack.sort()

result = 0
possible = []
for weight in backpack:
    while jewel and weight >= jewel[0][0]:
        heapq.heappush(possible, -heapq.heappop(jewel)[1])
    if possible:
        result -= heapq.heappop(possible)
print(result)