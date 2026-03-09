import sys

input = sys.stdin.readline
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()

answer = 0
start, end = points[0]
for x, y in points[1:]:
    if x > end:
        answer += end - start
        start, end = x, y
    else:
        end = max(end, y)
answer += end - start
print(answer)