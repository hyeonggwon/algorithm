import sys
from collections import deque

def bfs(start, target, l):
    queue = deque([start])
    graph[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                if nx == target[0] and ny == target[1]:
                    return graph[nx][ny]
                queue.append((nx, ny))
    return graph[target[0]][target[1]]


input = sys.stdin.readline
dx = [-2 , -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[-1] * l for _ in range(l)]
    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    print(bfs(start, target, l))