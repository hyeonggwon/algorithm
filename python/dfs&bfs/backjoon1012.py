import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, graph, m, n):
    queue = deque([start])
    x, y = start
    graph[y][x] = 2
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 2
                queue.append((nx, ny))

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cabbages = []
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        cabbages.append((x, y))
    answer = 0
    for x, y in cabbages:
        if graph[y][x] == 1:
            bfs((x, y))
            answer += 1
    print(answer)