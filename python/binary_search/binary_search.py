def binary_search_1(arr, target, start, end):
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_1(arr,target, start, mid - 1)
    else:
        return binary_search_1(arr, target, mid + 1, end)

def binary_search_2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

n = int(input())

result = binary_search_2(arr, n, 0, len(arr) - 1)
print("binary search 1")
if result is None:
    print("타겟을 찾을 수 없습니다.")
else:
    print(result + 1)

result = binary_search_2(arr, n, 0, len(arr) - 1)
print("binary search 2")
if result is None:
    print("타겟을 찾을 수 없습니다.")
else:
    print(result + 1)