from collections import deque

n, k = map(int, input().split())
def solution(n, k):
    dp = [0] * (100_001)
    if n >= k:
        return n - k
    queue = deque([n])
    while queue:
        v = queue.popleft()
        nexts = [v - 1, v + 1, v * 2]
        for next in nexts:
            if 0 <= next <= 100_000:
                cnt = dp[v] + 1
                if next == k:
                    return cnt
                if dp[next] == 0 or cnt < dp[next]:
                    dp[next] = cnt
                    queue.append(next)

print(solution(n, k))