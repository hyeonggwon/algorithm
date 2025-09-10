from itertools import combinations

EMPTY = 0
WALL = 1
ICE = 2

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y, dx, dy):
    graph[y][x] = ICE
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[ny][nx] != EMPTY:
            continue
        dfs(graph, nx, ny, dx, dy)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == EMPTY:
            count += 1
            dfs(graph, j, i, dx, dy)
print(count)

