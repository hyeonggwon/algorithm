import sys
from collections import deque

def bfs(graph, start, size, visited):
    queue = deque([start])
    start_x, start_y = start
    visited[start_x][start_y] = True
    targets = []
    dist = -1
    while queue:
        dist += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if 0 < graph[x][y] < size:
                targets.append((x, y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        if targets:
            targets.sort()
            target_x, target_y = targets[0]
            graph[target_x][target_y] = 0
            return dist, target_x, target_y
    else:
        return 0, -1, -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start = (0, 0)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0

size = 2
need = 2
answer = 0
x, y = start

while True:
    visited = [[False] * n for _ in range(n)]
    dist, x, y = bfs(graph, (x, y), size, visited)
    if dist:
        answer += dist
        need -= 1
        if need == 0:
            size += 1
            need = size
    else:
        break
print(answer)