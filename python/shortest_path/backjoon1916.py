import sys
import heapq

def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    cost_l[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost_l[now] < cost:
            continue
        for v, c in graph[now]:
            next_cost = cost + c
            if next_cost < cost_l[v]:
                cost_l[v] = next_cost
                heapq.heappush(q, (cost + c, v))

INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
cost_l = [INF] * (N + 1)

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
start, end = map(int, input().split())

dijkstra(graph, start)

print(cost_l[end])