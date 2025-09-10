from collections import deque

MONSTER = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, dx, dy):
    queue = deque([(0, 0)])
    while queue:
        v = queue.popleft()
        x = v[1]
        y = v[0]
        if x == m - 1 and y == n - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[ny][nx] != 1:
                continue
            queue.append((ny, nx))
            graph[ny][nx] = graph[y][x] + 1
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

result = bfs(graph, dx, dy)
print(result)

# from collections import deque
#
# MONSTER = 0
# SAFE = 1
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def bfs(graph, visited, dx, dy):
#     queue = deque()
#     childQueue = deque([(0, 0)])
#     visited[0][0] = True
#     result = 0
#     while childQueue:
#         result += 1
#         while childQueue:
#             queue.append(childQueue.popleft())
#         while queue:
#             v = queue.popleft()
#             x = v[1]
#             y = v[0]
#             if x == m - 1 and y == n - 1:
#                 return result
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[ny][nx] == MONSTER or visited[ny][nx]:
#                     continue
#                 childQueue.append((ny, nx))
#                 visited[ny][nx] = True
#     return result
#
# n, m = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
#
# result = bfs(graph, visited, dx, dy)
# print(result)