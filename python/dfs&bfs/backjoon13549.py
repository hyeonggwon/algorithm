import sys
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    dp[start] = 0
    while queue:
        x, sec = queue.popleft()
        walk_nx = [x - 1, x + 1]
        teleport_nx = 2 * x
        for nx in walk_nx:
            if 0 <= nx <= 100_000 and dp[nx] > sec + 1:
                dp[nx] = sec + 1
                queue.append((nx, sec + 1))
        if 0 <= teleport_nx <= 100_000 and dp[teleport_nx] > sec:
            dp[teleport_nx] = sec
            queue.append((teleport_nx, sec))

INF = sys.maxsize
n, k = map(int, input().split())
dp = [INF] * 100_001

bfs(n)

print(dp[k])