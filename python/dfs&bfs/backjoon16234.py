import sys
from collections import deque

def bfs(A, start, visited):
    queue = deque([start])
    start_x, start_y = start
    visited[start_x][start_y] = True
    union = []
    while queue:
        x, y = queue.popleft()
        union.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(A[nx][ny] - A[x][y]) <= r:
                queue.append((nx, ny))
                visited[nx][ny] = True
    country_cnt = len(union)
    if country_cnt > 1:
        sum_population = 0
        for x, y in union:
            sum_population += A[x][y]
        target_population = sum_population // country_cnt
        for x, y in union:
            A[x][y] = target_population
        return 1
    else:
        return 0

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    res_sum = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                res_sum += bfs(A, (i, j), visited)
    if res_sum == 0:
        break
    else:
        answer += 1

print(answer)