from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(starts):
    queue = deque(starts)
    result = -1
    while queue:
        result += 1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))
    return result

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
ripes = [(z, x, y) for z in range(h) for x in range(n) for y in range(m) if graph[z][x][y] == 1]

answer = bfs(ripes)
if any(0 in row for z_plane in graph for row in z_plane):
    print(-1)
else:
    print(answer)