import sys
import heapq

def dijkstra(dist, start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for v, c in graph[now]:
            next_cost = cost + c
            if next_cost < dist[v]:
                dist[v] = next_cost
                heapq.heappush(q, (cost + c, v))

INF = sys.maxsize
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist_start_1 = [INF] * (N + 1)
dist_start_v1 = [INF] * (N + 1)
dist_start_v2 = [INF] * (N + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dijkstra(dist_start_1, 1)
dijkstra(dist_start_v1, v1)
dijkstra(dist_start_v2, v2)

result = min(dist_start_1[v1] + dist_start_v1[v2] + dist_start_v2[N], dist_start_1[v2] + dist_start_v2[v1] + dist_start_v1[N])
print(-1 if result >= INF else result)