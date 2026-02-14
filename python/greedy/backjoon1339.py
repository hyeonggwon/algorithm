import sys

input = sys.stdin.readline
n = int(input())
words = [list(input().rstrip()) for _ in range(n)]
nums = [0] * (ord('Z') - ord('A') + 1)

for word in words:
    for i in range(len(word)):
        nums[ord(word[i]) - ord('A')] += 10 ** (len(word) - i - 1)

result = 0
nums.sort(reverse=True)

digit = 9
for num in nums:
    if num == 0:
        break
    result += digit * num
    digit -= 1
print(result)