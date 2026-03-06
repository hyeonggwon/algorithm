# import sys
#
# sys.setrecursionlimit(10**6)
#
# def dfs(graph, colors, v, color):
#     global is_valid
#     colors[v] = color
#     for u in graph[v]:
#         if colors[u] == color:
#             is_valid = False
#         if colors[u] == -1:
#             color = (color + 1) % 2
#             dfs(graph, colors, u, color)
#
# input = sys.stdin.readline
# K = int(input())
#
# for _ in range(K):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V + 1)]
#     colors = [-1] * (V + 1)
#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
#     is_valid = True
#     for i in range(1, V + 1):
#         if colors[i] == -1:
#             dfs(graph, colors, i, 0)
#     if is_valid:
#         print("YES")
#     else:
#         print("NO")

import sys
from collections import deque

def bfs(graph, colors, start):
    queue = deque([start])
    color = 0
    colors[start] = color
    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            for u in graph[v]:
                if colors[u] == color:
                    return -1
                if colors[u] == -1:
                    next_color = (color + 1) % 2
                    colors[u] = next_color
                    queue.append(u)
        color = (color + 1) % 2
    return 0

input = sys.stdin.readline
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [-1] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    res_sum = 0
    for i in range(1, V + 1):
        if colors[i] == -1:
            res_sum += bfs(graph, colors, i)
    if res_sum < 0:
        print("NO")
    else:
        print("YES")