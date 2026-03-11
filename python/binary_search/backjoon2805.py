import sys

input = sys.stdin.readline
N, M = map(int, input().split())
heights = list(map(int, input().split()))
left, right = 0, max(heights)

answer = 0
while left <= right:
    mid = (left + right) // 2
    sum_len = sum([x - mid if x - mid > 0 else 0 for x in heights])
    if sum_len < M:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1
print(answer)


