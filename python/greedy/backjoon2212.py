import sys
import heapq

# 목적은 최소 거리를 구하는 것이기 때문에, 센서 사이의 거리가 긴 것들을 K - 1 개 만큼 빼면 됨
# 먼저 센서 위치를 정렬한 후,
# 센서 사이의 거리를 우선순위 큐에 넣어서, 가장 거리가 큰 것들을 빼서 풀이
# 시간복잡도 : O(n log n)
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