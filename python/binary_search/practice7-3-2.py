def binary_search(heights, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum_heights = 0
        for height in heights:
            sum_heights += max(0, height - mid)
        if sum_heights >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n, m = map(int, input().split())
heights = list(map(int, input().split()))

MAX = 1_000_000_000

print(binary_search(heights, 0, MAX))

