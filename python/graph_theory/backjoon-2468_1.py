import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(start, h, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] - h > 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

result = 1
for h in range(1, 101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and graph[x][y] - h > 0:
                bfs((x, y), h, visited)
                cnt += 1
    result = max(result, cnt)
print(result)

