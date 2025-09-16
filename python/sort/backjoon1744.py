import bisect

n = int(input())
array = [int(input()) for _ in range(n)]
array.sort()

zero_right_index = bisect.bisect_right(array, 0)

minus_array = array[0:zero_right_index]
plus_array = array[zero_right_index:]

seq_sum = 0
i = 0
while i < len(minus_array) - 1:
    seq_sum += minus_array[i] * minus_array[i + 1]
    i += 2
if i == len(minus_array) - 1:
    seq_sum += minus_array[i]

i = len(plus_array) - 1
while i > 0:
    if plus_array[i - 1] == 1:
        seq_sum += plus_array[i - 1] + plus_array[i]
    else:
        seq_sum += plus_array[i - 1] * plus_array[i]
    i -= 2
if i == 0:
    seq_sum += plus_array[i]
print(seq_sum)