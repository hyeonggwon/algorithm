import sys

INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def solution():
    min_sum_abs = INF
    min_sum_nums = []
    for mid in range(1, len(arr) - 1):
        left = 0
        right = len(arr) - 1
        while left < mid and mid < right:
            current_sum = arr[left] + arr[mid] + arr[right]
            current_sum_abs = abs(current_sum)
            if current_sum_abs < min_sum_abs:
                min_sum_abs = current_sum_abs
                min_sum_nums = [arr[left], arr[mid], arr[right]]

            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                min_sum_nums = [arr[left], arr[mid], arr[right]]
                return min_sum_nums
    return min_sum_nums

print(*solution())