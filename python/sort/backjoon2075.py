import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N - 1):
    line = list(map(int, input().split()))
    for num in line:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

print(heap[0])