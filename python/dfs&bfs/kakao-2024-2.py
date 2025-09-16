import sys

sys.setrecursionlimit(10 ** 6)

MAX = 1_010_101
graph = [[] for _ in range(MAX + 1)]
reverse_graph = [[] for _ in range(MAX + 1)]
mapper = [-1] * MAX

def solution(edges):
    answer = [0] * 4

    n = 0
    visited = [False] * MAX
    for a, b in edges:
        if not visited[a]:
            n += 1
            mapper[a] = n
            visited[a] = True
        if not visited[b]:
            n += 1
            mapper[b] = n
            visited[b] = True

    for i in range(len(edges)):
        edges[i][0], edges[i][1] = mapper[edges[i][0]], mapper[edges[i][1]]

    for a, b in edges:
        graph[a].append(b)
        reverse_graph[b].append(a)

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

    target = []
    for x in result:
        if isDonut(x):
            answer[1] += 1
        elif isEight(x):
            answer[3] += 1
        else:
            target.append(x)

    for x in target:
        if len(graph[x[0]]) >= 2:
            answer[0] = mapper.index(x[0])
        if len(graph[x[0]]) == 0:
            answer[2] += 1

    return answer

def isDonut(arr):
    node_count = len(arr)
    edge_count = 0
    for node in arr:
        edge_count += len(graph[node])
    if edge_count != node_count:
        return False
    if node_count == 1:
        return graph[arr[0]][0] == arr[0]
    return True

def isEight(arr):
    if len(arr) < 3:
        return False
    node_count = len(arr)
    edge_count = 0
    for node in arr:
        edge_count += len(graph[node])
    return edge_count - 1 == node_count

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