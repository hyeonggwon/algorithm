import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

nums.sort()

def solution():
    answer = 0
    for target_idx in range(N):
        left = 0
        right = N - 1
        while left < right:
            if left == target_idx:
                left += 1
                continue
            if right == target_idx:
                right -= 1
                continue

            current_sum = nums[left] + nums[right]

            if current_sum == nums[target_idx]:
                answer += 1
                break
            if current_sum < nums[target_idx]:
                left += 1
            elif current_sum > nums[target_idx]:
                right -= 1
    return answer

print(solution())
