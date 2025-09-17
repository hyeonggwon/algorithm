import sys

def binary_search(start, end):
    result = 1
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for l in lengths:
            cnt += l // mid
        if cnt < n:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

input = sys.stdin.readline

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]

MAX = 2 ** 31 - 1

print(binary_search(1, MAX))