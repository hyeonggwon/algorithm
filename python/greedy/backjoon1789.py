import sys

input = sys.stdin.readline
s = int(input())
result = 0
for i in range(1, s):
    if s - i <= i:
        break
    s -= i
    result += 1

result += 1
print(result)