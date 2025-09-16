from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(starts):
    queue = deque(starts)
    child_queue = deque()
    result = -1
    while child_queue or queue:
        result += 1
        while child_queue:
            queue.append(child_queue.popleft())
        while queue:
            v = queue.popleft()
            x = v[0]
            y = v[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] != 0:
                    continue
                graph[nx][ny] = 1
                child_queue.append((nx, ny))
    return result

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ripes = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 1]

answer = bfs(ripes)
isAllRipe = True
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            isAllRipe = False
if isAllRipe:
    print(answer)
else:
    print(-1)