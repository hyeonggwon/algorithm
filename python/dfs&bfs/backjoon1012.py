import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = deque([start])
    x = start[0]
    y = start[1]
    graph[y][x] = 2
    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or graph[ny][nx] != 1:
                continue
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