from collections import deque

def bfs(graph, start, visited, path_map):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                queue.append(u)
                path_map[start][u] = 1
                visited[u] = True

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    sub_graph = list(map(int, input().split()))
    for j in range(n):
        if sub_graph[j] == 1:
            graph[i].append(j)

path_map = [[0] * n for _ in range(n)]
for i in range(n):
    visited = [False] * n
    bfs(graph, i, visited, path_map)

for i in range(n):
    print(*path_map[i])
