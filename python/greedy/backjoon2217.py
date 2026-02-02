import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1

result = 0
remainder = n
for i in range(1, 10001):
    if arr[i] == 0: continue
    result = max(result, i * remainder)
    remainder -= arr[i]

print(result)