import sys

def dfs(graph, v, visited):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)

print(sum(visited) - 1)