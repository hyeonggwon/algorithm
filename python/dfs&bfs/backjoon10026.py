import copy
import sys
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    color = graph[start[0]][start[1]]
    graph[start[0]][start[1]] = 'V'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                graph[nx][ny] = 'V'
                queue.append((nx, ny))

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
color_weak_graph = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if color_weak_graph[i][j] == 'G':
            color_weak_graph[i][j] = 'R'

cnt1 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 'V':
            bfs(graph, (i, j))
            cnt1 += 1

cnt2 = 0
for i in range(n):
    for j in range(n):
        if color_weak_graph[i][j] != 'V':
            bfs(color_weak_graph, (i, j))
            cnt2 += 1

print(cnt1, cnt2)