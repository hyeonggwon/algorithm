import sys
import heapq

input = sys.stdin.readline
N = int(input())
K = int(input())
nums = list(map(int, input().split()))
nums.sort()
dist_q = [nums[i] - nums[i + 1] for i in range(N - 1)]

heapq.heapify(dist_q)

for _ in range(K - 1):
    if not dist_q:
        break
    heapq.heappop(dist_q)

print(-sum(dist_q))