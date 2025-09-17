import sys

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        current = houses[0]
        cnt = 1
        for i in range(len(houses)):
            if houses[i] >= current + mid:
                current = houses[i]
                cnt += 1
        if cnt < c:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

input = sys.stdin.readline
n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

print(binary_search(1, houses[-1] - houses[0]))