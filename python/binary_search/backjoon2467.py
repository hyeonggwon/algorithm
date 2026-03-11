import sys

def solution(values):
    left = 0
    right = len(values) - 1
    min_sum_abs = sys.maxsize
    min_sum_nums = [0, 0]
    while left < right:
        cur_sum = values[left] + values[right]
        cur_sum_abs = abs(cur_sum)
        if min_sum_abs > cur_sum_abs:
            min_sum_abs = cur_sum_abs
            min_sum_nums = [values[left], values[right]]
        if cur_sum < 0:
            left += 1
        elif cur_sum > 0:
            right -= 1
        else:
            break
    return min_sum_nums

input = sys.stdin.readline
N = int(input())
values = list(map(int, input().split()))

values.sort()

print(*solution(values))
