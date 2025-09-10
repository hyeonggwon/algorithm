from collections import deque

WALL = 0

def bfs(graph, start):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([start])
    while queue:
        v = queue.popleft()
        x = v[1]
        y = v[0]
        if x == m - 1 and y == n - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[ny][nx] == WALL or graph[ny][nx] != 1:
                continue
            graph[ny][nx] = graph[y][x] + 1
            queue.append((ny, nx))
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = bfs(graph, (0, 0))
print(result)
