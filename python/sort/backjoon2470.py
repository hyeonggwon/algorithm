import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort(key = abs)

min_sum = sys.maxsize
for i in range(1, n):
    cur_sum = abs(array[i - 1] + array[i])
    if cur_sum < min_sum:
        min_sum = cur_sum
        min_pair = [array[i - 1], array[i]]
min_pair.sort()
print(*min_pair)