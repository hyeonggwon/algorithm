from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

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
            z = v[0]
            x = v[1]
            y = v[2]
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nz][nx][ny] != 0:
                    continue
                graph[nz][nx][ny] = 1
                child_queue.append((nz, nx, ny))
    return result

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
ripes = [(z, x, y) for z in range(h) for x in range(n) for y in range(m) if graph[z][x][y] == 1]

answer = bfs(ripes)
isAllRipe = True
for z in range(h):
    for x in range(n):
        for y in range(m):
                if graph[z][x][y] == 0:
                    isAllRipe = False
if isAllRipe:
    print(answer)
else:
    print(-1)