import sys
input = sys.stdin.readline
n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
min_price = 1_000_000_001
for i in range(n - 1):
    min_price = min(min_price, prices[i])
    result += min_price * distances[i]

print(result)