from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(starts):
    queue = deque(starts)
    result = -1
    while queue:
        result += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
    return result

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ripes = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 1]

answer = bfs(ripes)
if any(0 in row for row in graph):
    print(-1)
else:
    print(answer)