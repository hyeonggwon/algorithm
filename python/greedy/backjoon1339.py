import sys

input = sys.stdin.readline
n = int(input())
words = [list(input().rstrip()) for _ in range(n)]
nums = [0] * (ord('Z') - ord('A') + 1)

for word in words:
    for i in range(len(word)):
        nums[ord(word[i]) - ord('A')] += 10 ** (len(word) - i - 1)

result = 0
for i in range(9, 0, -1):
    print(i, end=' ')
    max_num = 0
    max_num_j = 0
    for j in range(len(nums)):
        if nums[j] > max_num:
            max_num = nums[j]
            max_num_j = j
    result += i * max_num
    nums[max_num_j] = 0
print(result)