INF = int(1e9)
n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
dp = [INF] * 10001

dp[0] = 0
for i in range(1, m + 1):
    for money in moneys:
        if i - money >= 0:
            dp[i] = min(dp[i], dp[i - money] + 1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])