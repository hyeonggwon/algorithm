import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    dp[start] = 0
    while queue:
        x = queue.popleft()
        teleport_nx = 2 * x
        if 0 <= teleport_nx <= 100_000 and dp[teleport_nx] > dp[x]:
            dp[teleport_nx] = dp[x]
            queue.appendleft(teleport_nx)
        for walk_nx in [x - 1, x + 1]:
            if 0 <= walk_nx <= 100_000 and dp[walk_nx] > dp[x] + 1:
                dp[walk_nx] = dp[x] + 1
                queue.append(walk_nx)

INF = sys.maxsize
n, k = map(int, input().split())
dp = [INF] * 100_001

bfs(n)

print(dp[k])