import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
avg = sum(nums) / n
mid = nums[n // 2]
mostCommon = Counter(nums).most_common(2)
if len(mostCommon) >= 2 and mostCommon[0][1] == mostCommon[1][1]:
    mostFrequent = mostCommon[1][0]
else:
    mostFrequent = mostCommon[0][0]
arrange = nums[-1] - nums[0]
print(round(avg))
print(mid)
print(mostFrequent)
print(arrange)