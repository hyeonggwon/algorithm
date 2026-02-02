import sys
sys.setrecursionlimit(10 ** 6)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(v, h, visited, stack):
    x, y = v[0], v[1]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] - h > 0 and not visited[nx][ny]:
            dfs((nx, ny), h, visited, stack)
    stack.append(v)

def reverse_dfs(v, h, visited, stack):
    x, y = v[0], v[1]
    visited[x][y] = True
    stack.append(v)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] - h > 0 and not visited[nx][ny]:
            dfs((nx, ny), h, visited, stack)

result = 1
for h in range(1, 101):
    stack = []
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and graph[x][y] - h > 0:
                dfs((x, y), h, visited, stack)

    visited = [[False] * n for _ in range(n)]
    scc_list = []
    while stack:
        v = stack.pop()
        x, y = v[0], v[1]
        if not visited[x][y]:
            scc = []
            reverse_dfs((x, y), h, visited, scc)
            scc_list.append(sorted(scc))
    result = max(result, len(scc_list))
print(result)

