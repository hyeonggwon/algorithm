from collections import deque
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(walls):
    grid = [row[:] for row in origin_grid]

    for i, j in walls:
        grid[i][j] = 1

    queue = deque(virus_spaces)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 0:
                continue
            grid[nx][ny] = 2
            queue.append((nx, ny))
    return sum(row.count(0) for row in grid)

n, m = map(int, input().split())
origin_grid = [list(map(int, input().split())) for _ in range(n)]

empty_spaces = [(i, j) for i in range(n) for j in range(m) if origin_grid[i][j] == 0]
virus_spaces = [(i, j) for i in range(n) for j in range(m) if origin_grid[i][j] == 2]

result = 0
for walls in combinations(empty_spaces, 3):
    result = max(result, bfs(walls))
print(result)