import sys
from collections import deque

# 북, 서, 남, 동 (시작점 그래프와 끝점 그래프를 나누기 위함)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(graph, start, dist):
    queue = deque([start])
    x = start[0]
    y = start[1]
    graph[x][y] = dist
    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

input = sys.stdin.readline
n, m = map(int, input().split())
# 시작점 그래프
graph_left = [list(map(int, input().rstrip())) for _ in range(n)]
# 끝점 그래프
graph_right = [row[:] for row in graph_left]
walls = [(x, y) for x in range(n) for y in range(m) if graph_left[x][y] == 1]

bfs(graph_left, (0, 0), 2)
bfs(graph_right, (n - 1, m - 1), 2)

min_dist = sys.maxsize if graph_left[n - 1][m - 1] == 0 else graph_left[n - 1][m - 1] - 1
for (x, y) in walls:
    min_prev_dist = sys.maxsize
    for i in range(2):
        px = x + dx[i]
        py = y + dy[i]
        if 0 <= px < n and 0 <= py < m and graph_left[px][py] >= 2:
            min_prev_dist = min(min_prev_dist, graph_left[px][py])
    min_next_dist = sys.maxsize
    for i in range(2, 4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph_right[nx][ny] >= 2:
            min_next_dist = min(min_next_dist, graph_right[nx][ny])
    if min_prev_dist != sys.maxsize and min_next_dist != sys.maxsize:
        min_dist = min(min_dist, (min_prev_dist + min_next_dist) - 1)
if min_dist == sys.maxsize:
    print(-1)
else:
    print(min_dist)