def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
parts = list(map(int, input().split()))

m = int(input())
target_parts = list(map(int, input().split()))

parts.sort()

for target in target_parts:
    result = binary_search(parts, target, 0, len(parts) - 1)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')