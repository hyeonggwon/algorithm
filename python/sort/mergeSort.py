def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))


def merge(left, right):
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)

arr = [10, 8, 7, 1, 2, 5, 4, 3, 3, 2, 7, 8]
arr2 = [10, 8, 7, 1, 2, 5, 4, 3, 3, 2, 7, 8]
print(mergeSort(arr))
quickSort(arr2, 0, len(arr2) - 1)
print(arr2)