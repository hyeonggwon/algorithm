import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
def setting(x):
    if x < 0:
        return -x
    else:
        return x
array.sort(key = setting)

min_sum = sys.maxsize
for i in range(1, n):
    cur_sum = abs(array[i - 1] + array[i])
    if cur_sum < min_sum:
        min_sum = cur_sum
        min_pair = [array[i - 1], array[i]]

min_pair = reversed(min_pair) if min_pair[1] < 0 else min_pair
print(*min_pair)