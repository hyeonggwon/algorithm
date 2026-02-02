import sys
from collections import deque

def bfs(graph, start, parent):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                queue.append(u)
                visited[u] = True

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, parent)

print(*parent[2:], sep='\n')
