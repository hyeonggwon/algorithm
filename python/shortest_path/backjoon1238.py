import heapq
import sys

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]
distance_from_x = [INF] * (n + 1)
distance_to_x = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reversed_graph[b].append((a, c))

dijkstra(x, graph, distance_from_x)
dijkstra(x, reversed_graph, distance_to_x)

distance_sum_list = [distance_from_x[i] + distance_to_x[i] for i in range(n + 1)]
max_distance_sum = 0
for d in distance_sum_list:
    if d < INF:
        max_distance_sum = max(max_distance_sum, d)
print(max_distance_sum)

