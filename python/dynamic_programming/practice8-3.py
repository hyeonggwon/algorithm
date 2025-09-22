n = int(input())
foods = list(map(int, input().split()))
k = len(foods)
dp = [0] * k

dp[0], dp[1] = foods[0], max(foods[0], foods[1])

for i in range(2, k):
    dp[i] = max(dp[i - 2] + foods[i], dp[i - 1])

print(dp[k - 1])