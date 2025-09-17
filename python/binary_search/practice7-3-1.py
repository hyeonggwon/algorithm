def binary_search(heights, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_heights = 0
        for height in heights:
            sum_heights += max(0, height - mid)
        if sum_heights == m:
            return mid
        elif sum_heights > m:
            start = mid + 1
        else:
            end = mid - 1
    return end

n, m = map(int, input().split())
heights = list(map(int, input().split()))

MAX = 1_000_000_000

print(binary_search(heights, 0, MAX))

