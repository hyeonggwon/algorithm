import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N - 1):
    line = list(map(int, input().split()))
    for i in range(N):
        if line[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, line[i])

print(heap[0])