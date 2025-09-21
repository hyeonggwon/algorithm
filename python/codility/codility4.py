def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

def merge(left, right):
    global cnt
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            cnt += len(right) - j
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

cnt = 0

def solution(A):
    # Implement your solution here
    MAX = 1_000_000_000
    merge_sort(A)
    return cnt if cnt <= MAX else -1


A = [2, 4, 6, 2, 2, 5, 4]
A = [2, 1]
print(solution(A))