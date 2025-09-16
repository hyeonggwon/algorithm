n = 12
edges = [[1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 5], [1, 7], [7, 8], [8, 9], [9, 7], [7, 10], [10, 11], [11, 12], [12, 7]]
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

def solution(edges):
    for edge in edges:
        graph[edge[0]].append(edge[1])
        reverse_graph[edge[1]].append(edge[0])

    stack = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, stack)

    result = []
    visited = [False] * (n + 1)
    while stack:
        scc = []
        node = stack.pop()
        if not visited[node]:
            reverse_dfs(node, visited, scc)
            result.append(sorted(scc))
    print(result)

def dfs(v, visited, stack):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited, stack)
    stack.append(v)

def reverse_dfs(v, visited, stack):
    visited[v] = True
    stack.append(v)
    for u in reverse_graph[v]:
        if not visited[u]:
            reverse_dfs(u, visited, stack)

solution(edges)