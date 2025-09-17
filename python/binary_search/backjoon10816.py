import bisect
m = int(input())
nums = list(map(int, input().split()))

n = int(input())
targets = list(map(int, input().split()))

nums.sort()
result = [bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target) for target in targets]
print(*result)